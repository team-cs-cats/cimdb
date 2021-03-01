# webapp.py
from flask import Flask, render_template, flash
from flask import request, redirect

# add jsonify to handle converting filter search results to html
from flask import jsonify 

# add json to handle db connection
from flask import json

# import these to handle user accounts
from flask import url_for, session
import flask_login
from flask_login import login_user, current_user, logout_user, login_required

# import a local python script to generate new passwords
import cim.static.py.password_generator as pw_gen

# perform a local import to load the dummy data
from cim.dummy_data import DummyData

# connect to databse
import cim.database.db_connector as db

# import basic queries that are used in multiple routes
import cim.database.db_queries as dbq

# import INSERT queries as dbiq
import cim.database.db_insert_queries as dbiq

# import UPDATE queries as dbiq
import cim.database.db_update_queries as dbuq

# import DELETE queries as dbdq
import cim.database.db_delete_queries as dbdq

# import filter SELECT queries as dbfq
import cim.database.db_filter_queries as dbfq

# resolve CORS issues for local development
from flask_cors import CORS, cross_origin

# for backend processes
import random

#create the web application
webapp = Flask(__name__)
CORS(webapp)

# added a 'secret' key for user management
webapp.secret_key = 'Team CS Cats'


# Set up login manager to handle basic user authentication
login_manager = flask_login.LoginManager()
login_manager.init_app(webapp)

# Create a connection to the database
db_connection = db.connect_to_database()


# Load dummy data for the webpages to reference
data = DummyData()


# Set up a mock set of user ids to use for our logins (this can be moved/replaced later)
users = {}

for employee in data.get_emp():
	emp_email = employee["employee_email"]
	emp_pass = employee["employee_password"]
	users[emp_email] = {'password': emp_pass}


# Create a basic user class
class User(flask_login.UserMixin):
	pass


# Associate the login manager with the users provided, unless the user provided isn't on the allowed dictionary
@login_manager.user_loader
def user_loader(email):

	# if the email provided is not in the prepopulated user database, return nothing
	if email not in users:
		return

	# otherwise, initiate a new user based on the provided email and return it
	user = User()
	user.id = email
	return user

# Associate a logged in user with the current session
@login_manager.request_loader
def request_loader(request):

	# obtain the current email
	email = request.form.get('email')

	# if the current email isn't on the list of allowed users, return nothing
	if email not in users:
		return

	# if the user email is allowed, set it as the id of the current user
	user = User()
	user.id = email
	user.is_authenticated = request.form['password'] == users[email]['password']
	return user

# Add an association for any unauthorized session logins.
@login_manager.unauthorized_handler
def unauthorized_handler():
	return 'Unauthorized'




#provide a route for the index of the webpage requests on the web application can be addressed
@webapp.route('/', methods=['GET', 'POST'])
def index():
	"""The webapp's landing page."""

	# if the user attempts to login, but provides no info, refresh the page
	if request.method == 'GET':
		return render_template("index.html")

	# if the user attempts to login with info, check to see if their info is valid
	email = request.form['email']
	if request.form['password'] == users[email]['password']:

		# If valid credentials, sign the user into the Work Orders page
		user = User()
		user.id = email
		flask_login.login_user(user)
		return redirect(url_for('workorders'))

	# If the user provided bad credentials, return them to the index page (TODO: flash error)
	return render_template("index.html")


# Provide a route to redirect a logged in user to the orders page web app
@webapp.route('/login', methods=['GET', 'POST'])
def login():

	
	# if the user attempts to login, but provides no info, refresh the page
	if request.method == 'GET':
		return render_template("index.html")

	# if the user attempts to login with info, check to see if their info is valid
	email = request.form['email']

	if email not in users:
		return redirect(url_for('index'))

	if request.form['password'] == users[email]['password']:

		# If valid credentials, sign the user into the Work Orders page
		user = User()
		user.id = email

		# determine the employee ID of the user email provided
		employee_details = None
		for employee_info in data.get_emp():
			if employee_info['employee_email'] == email:
				user.employee_details = employee_info

				print('HERE', type(user.employee_details))
				break

		# if we couldn't find the details, redirect to the index
		if user.employee_details is None:
			return redirect(url_for('index'))

		# otherwise use the id to save the employee details and render the landing page
		user_first_name = user.employee_details['employee_first_name']
		user_last_name = user.employee_details['employee_last_name']
		user_email = user.employee_details['employee_email']
		user_id = user.employee_details['employee_id']
		user_site_id = user.employee_details['employee_site_id']
		user_group = user.employee_details['employee_group'].capitalize()
		flask_login.login_user(user)
		session['user_first_name'] = user_first_name
		return redirect(url_for('landing', 
			user_first_name=user_first_name, 
			user_last_name=user_last_name, 
			user_email=user_email, 
			user_id=user_id, 
			user_site_id=user_site_id,
			user_group=user_group
			))

	# If the user provided bad credentials, return them to the index page (TODO: flash error)
	return render_template("index.html")


# Provide a route to log out the web app
@webapp.route('/logout', methods=['GET', 'POST'])
def logout():

	flask_login.logout_user()
	return redirect(url_for("index"))


@webapp.route('/workorders', methods=['GET', 'POST'])
@login_required
def workorders():
	"""The webapp's page for work orders, which allows reviewing and adding work orders."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		error = 'You are not logged in. Please log in to view this page.'
		return redirect(url_for("cim.templates.index", error))

	# otherwise, return the workorders page
	if request.method=="GET":

		# get information from DB
		workorder_results=dbq.get_db_work_orders()
		employee_results=dbq.get_db_employees()
	

		return render_template("workorders.html",
								employees=employee_results ,
								workorders=workorder_results
								)

	if request.method=="POST":
		id=request.json["id"]
		date=request.json["date"]
		reference=request.json["reference"]
		dbiq.insert_work_order(date,None,"assembly_pending",int(reference),id)
		print(f'got a post request! id is: {id} and date is: {date} and reference is{reference}')
		return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
		


@webapp.route('/landing', methods=['GET', 'POST'])
@login_required
def landing():
	"""The webapp's logged in landing page, which allows an employee to access the internal links."""

	# otherwise, return the landing page and pass it the employee ID which can be used as a key
	if request.method=="GET":

		# determine the number of work orders currently assigned to the current employee
		wo_count = 0
		for work_order in data.get_wo():
			if work_order['wo_employee_id'] == request.args.get('user_id'):
				wo_count += 1


		return render_template("landing.html", 
			user_first_name=request.args.get('user_first_name'),
			user_last_name=request.args.get('user_last_name'),
			user_email=request.args.get('user_email'),
			user_id=request.args.get('user_id'),
			user_site_id=request.args.get('user_site_id'),
			user_group=request.args.get('user_group'),
			sites = data.get_sites(),
			work_order_count = wo_count
			)

@webapp.route('/products', methods=['GET', 'POST'])
@login_required
def products():
	"""The webapp's page for viewing an employee's currently assigned products to assemble and QC."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	if request.method=="GET":
		return render_template("products.html")


@webapp.route('/inventory-spec', methods=['GET', 'POST'])
@login_required
def inventory_special_components():
	"""The webapp's page for viewing the inventory.
	This allows the employee to review existing stock and order new stock of standard and special components."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	if request.method=="GET":
		return render_template("inventory_special_comps.html", 
			special_components=data.get_sc(), 
			sites=data.get_sites(),
			special_components_catalog=data.get_sp_catalog()
			)


@webapp.route('/inventory-reg', methods=['GET', 'POST'])
@login_required
def inventory_regular_components():
	"""The webapp's page for viewing the inventory.
	This allows the employee to review existing stock and order new stock of standard and special components."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	# Load location results from the database (or the dummy data if the database doesn't work)
	regular_component_results = dbq.get_db_regular_components()

	# regular comps by location 
	reg_comp_location_details = dbq.get_db_regular_components_by_location()

	# Load site results from the database (or the dummy data if the database doesn't work)
	site_results = dbq.get_db_sites()


	if request.method=="GET":
		return render_template("inventory_regular_comps.html", 
			regular_components=regular_component_results, 
			reg_comp_locations=reg_comp_location_details, 
			sites=site_results)

	if request.method == "POST":
		filter_search_box = request.form.get("text")
		filtered_reg_comp_results = dbfq.get_filtered_regular_components(filter_search_box)
		return jsonify(filtered_reg_comp_results)


@webapp.route('/shipping', methods=['GET', 'POST'])
@login_required
def shipping():
	"""The webapp's page for viewing the shipping status of work orders.
	This allows the employee to review existing work orders and see if they are ready to ship or not."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	# Load work order results from the database (or the dummy data if the database doesn't work)
	work_order_results = dbq.get_db_work_orders()

	# Load work order results from the database (or the dummy data if the database doesn't work)
	employee_results = dbq.get_db_employees()

	if request.method=="GET":
		return render_template("shipping.html", work_orders=work_order_results, employees=employee_results)

@webapp.route('/locations', methods=['GET', 'POST'])
@login_required
def locations():
	"""The webapp's page for viewing the locations at the various sites, 
	as well as which regular components, special components, and products are placed in which locations."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	# Load location results from the database (or the dummy data if the database doesn't work)
	location_results = dbq.get_db_locations()

	# Load site results from the database (or the dummy data if the database doesn't work)
	site_results = dbq.get_db_sites()

	if request.method=="GET":
		return render_template("locations.html", 
		locations=location_results, products=data.get_products(), regular_components=data.get_rc(), special_components=data.get_sc(), sites=site_results)

	# if post request perform insertion of new location
	if request.method=="POST":

		# refactored to pull from json TODO
		# provided_add_new_location_site = request.json['add_new_location_site']
		# provided_add_location_room_number = request.json['add_location_room_number']
		# provided_add_location_shelf_number = request.json['add_location_shelf_number']

		# # obtain data from new location form
		provided_add_new_location_site = request.form['add_new_location_site']
		provided_add_location_room_number = request.form['add_location_room_number']
		provided_add_location_shelf_number = request.form['add_location_shelf_number']	

		# perform the insertion
		dbiq.insert_location(
			new_location_room_number=provided_add_location_room_number, 
			new_location_shelf_number=provided_add_location_shelf_number, 
			new_location_site_id=provided_add_new_location_site)

		# Ali's json method
		# return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
		
		return render_template("locations.html", 
		locations=location_results, products=data.get_products(), regular_components=data.get_rc(), special_components=data.get_sc(), sites=site_results)

@webapp.route('/employee-mgmt', methods=['GET', 'POST'])
@login_required
def employee_management():
	"""The webapp's page for managing current sites. This allows a manager to update information about current sites."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	# Load site results from the database (or the dummy data if the database doesn't work)
	site_results = dbq.get_db_sites()

	# Load employee results from the database (or the dummy data if the database doesn't work)
	employee_results = dbq.get_db_employees()

	if request.method=="GET":
		return render_template("employee_mgmt.html", sites=site_results, employees=employee_results)

	if request.method=="POST":

		# obtain data from new site form
		provided_employee_fname = request.form['new_employee_fname']
		provided_employee_lname = request.form['new_employee_lname']
		provided_employee_email = request.form['new_employee_email']
		provided_employee_group = request.form['new_employee_group']
		provided_employee_site_id = request.form['new_employee_site']	

		# generate a password
		generated_password = pw_gen.new_password(size=8)

		# perform the insertion
		dbiq.insert_employee(new_employee_first_name=provided_employee_fname, 
			new_employee_last_name=provided_employee_lname, 
			new_employee_email=provided_employee_email, 
			new_employee_group=provided_employee_group, 
			new_employee_password=generated_password,
			new_employee_site_id=provided_employee_site_id)

		return render_template("employee_mgmt.html", sites=site_results, employees=employee_results)


@webapp.route('/site-mgmt', methods=['GET', 'POST'])
@login_required
def site_management():
	"""The webapp's page for managing current sites. This allows a manager to update information about current sites."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	# Load site results from the database (or the dummy data if the database doesn't work)
	site_results = dbq.get_db_sites()
	
	if request.method=="GET":
		return render_template("site_mgmt.html", sites=site_results, states=data.get_states())

	if request.method=="POST":

		# obtain data from new site form
		provided_site_address_1 = request.form['new_site_address_1']
		provided_site_address_2 = request.form['new_site_address_2']
		provided_site_city = request.form['new_site_city']
		provided_site_state = request.form['new_site_state']
		provided_site_zip = request.form['new_site_zip']

		print('provided_site_address_2 is', provided_site_address_2)

		# perform the insertion
		dbiq.insert_site(new_site_address_1=provided_site_address_1, 
			new_site_address_2=provided_site_address_2, 
			new_site_city=provided_site_city, 
			new_site_state=provided_site_state, 
			new_site_zip=provided_site_zip)

		return render_template("site_mgmt.html", sites=site_results, states=data.get_states())

# workorder details. it takes the wo_id as argument to retrive the the information from DB
@webapp.route('/wo-details', methods=['GET', 'POST'])
@login_required
def wo_details(wo_id=""):
	"""The webapp's page takes wo_id and retirve the inforamtion from DB."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	if request.method=="GET":

		if request.args.get("wo_id"):
			wo_id=request.args.get("wo_id")
				

		# # get wo products information:
		# if wo_id:
		# 	products=data.get_workorderproducts()[wo_id]
		# else:
		# 	products={}
		

		#get products catalog
		products_catalog=data.get_products_catalog()
		
		# print(f'############ wo_id is : {wo_id}')
		# print(f'############ products are is : {products}')

		
		if wo_id !="":
			products=dbq.get_db_workorder_details(str(wo_id))
			workorder_information=dbq.get_a_work_order(wo_id)
			# print("***************************************")
			# print(f'workorder_id is: {wo_id}')
			# print(f'products is: {products}')
			# print(f'workorder_information is: {workorder_information}')
		
			
		else:
			products={}
			workorder_information={}

		# products=dbq.get_db_workorder_details(str(879845))

		# render the detail page
		return render_template("wo-details.html",
								wo_id=wo_id,
								products_catalog=products_catalog ,
								products=products,
								workorder_information=workorder_information
								)

	if request.method=="POST":

		# for development 
		#  dbq.rev_update_is_free(101711)
		# return

		print(f'got a post request! and request.json is: {request.json}')
				
		# make a new product with the first avaible product and assign it to this work order
		# the default location is assembly department

		free_sc=dbq.get_free_sc_sn(request.json["sc_pn"])
		product_sc_sn=free_sc[0]["sc_sn"]
				
		product_pn=request.json["product_pn"]
		product_family=request.json["product_family"]
		employee_id=request.json["employee_id"]
		product_location=10

		
		# dates are set to None
		product_assmebly_date=None
		product_qc_date=None
		product_warranty_date=None

		# insert product
		dbiq.insert_product(product_pn,product_family,product_assmebly_date,product_qc_date,
		product_warranty_date,employee_id,product_location,product_sc_sn)

		# update is_free attr
		dbq.update_is_free(product_sc_sn)
				

		# get product_sn using its SC_sn
		product_sn=dbq.get_product_sn(product_sc_sn)

		if product_sn==-1:
			# TODO: return error
			pass

		else:
			# add to work order
			wo_id=request.json["wo_id"]
			dbiq.insert_work_order_products(wo_id,product_sn)

		return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


# products details. it takes the product_sn as argument to retrive the the information from DB
@webapp.route('/product-details', methods=['GET', 'POST'])
@login_required
def product_details(product_sn=""):
	"""The webapp's page takes product_sn and retirve the inforamtion from DB."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	if request.method=="GET":

		if request.args.get("product_sn"):
			product_sn=request.args.get("product_sn")
		

		# get product information:
		if product_sn != "":
			product=dbq.get_db_product_details(product_sn)
								
		else:
			product={}
		
		
		# get components information:
		if product_sn != "":
			components_from_db=dbq.get_db_product_components(product_sn)

			# make a custom object from query result
			components={}
			for item in components_from_db:
				# print(f'item is: {item}')
				components[item["rc_category"]]=item["rc_pn_desc"]
				components[item["rc_category"]+"_quant"]=item["prc_quantity_needed"]

			print(f'temp is {components}')
								
		else:
			components={}
		
					
		#get reqular components catalog
		regular_components_catalog=data.get_rc_catalog()

		#get special components catalog
		special_components_catalog=data.get_sp_catalog()
		
	
		# render the detail page
		return render_template("product-details.html",product=product,components=components,special_components_catalog=special_components_catalog,regular_components_catalog=regular_components_catalog)

	if request.method=="POST":

		# dbiq.insert_products_regular_comps(10,2000,500)

		print(f'got a post request! and request.json is: {request.json}')

		# create correct object using post data
		product_sn=request.json['product_sn']
		regular_componenets=[
			{'rc_pn':dbq.get_db_regular_component_pn(request.json['MB'])[0]['rc_pn'],'quant':1}, # MB Data
			{'rc_pn':dbq.get_db_regular_component_pn(request.json['Case'])[0]['rc_pn'],'quant':1}, # Case Data
			{'rc_pn':dbq.get_db_regular_component_pn(request.json['GC'])[0]['rc_pn'],'quant':1}, # GC Data
			{'rc_pn':dbq.get_db_regular_component_pn(request.json['RAM'])[0]['rc_pn'],'quant':request.json['RAM_quant']}, # RAM Data
			{'rc_pn':dbq.get_db_regular_component_pn(request.json['HDD'])[0]['rc_pn'],'quant':request.json['HDD_quant']}, # HDD Data
		]


		
		# add compoenents into table

		for component in regular_componenets:
			dbiq.insert_products_regular_comps(product_sn,component['rc_pn'],component['quant'])

		 		
		# TODO: adjust RC quantity
		
		return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
				

		
# Assembly page. The page lists are assigned products ready for assembly 
@webapp.route('/assembly', methods=['GET', 'POST'])
@login_required
def assembly():
	"""The webapp's page retirve the inforamtion from DB for the Assembly process."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	if request.method=="GET":

		# get employee ID

		employee_id=None

		# assembly_list=data.get_assembly()

		assembly_list=dbq.get_assembly_list(employee_id)

		print(f'assembly is: {assembly_list}')

		products_catalog=data.get_products_catalog()
		
		
		# render the assembly page
		return render_template("assembly.html",assembly_list=assembly_list,products_catalog=products_catalog)


# QC page. The page lists are assigned products ready for assembly 
@webapp.route('/qc', methods=['GET', 'POST'])
@login_required
def QC():
	"""The webapp's page retirve the inforamtion from DB for the Assembly process."""

	# if the current user is not authenticated, redirect the user to the logged out index page
	if not current_user.is_authenticated:
		return redirect(url_for("cim.templates.index"))

	if request.method=="GET":
		# get employee ID

		employee_id=None

		# assembly_list=data.get_assembly()

		qc_list=dbq.get_qc_list(employee_id)

		print(f'qc is: {qc_list}')

		products_catalog=data.get_products_catalog()
		
		# render the assembly page
		return render_template("qc.html",qc_list=qc_list,products_catalog=products_catalog)

@webapp.route('/data/product_catalog', methods=['GET', 'POST'])
@login_required
def get_products_catalog_r():
	# returns products catalog
	if request.method=="GET":
		print(data.get_products_catalog())
		return data.get_products_catalog()


@webapp.route('/data/free_sn', methods=['GET', 'POST'])
@login_required
def get_free_sc_sn():
	# Returns a valid free SC_SN based on the given PN and Method

	if request.method=="POST":
		
		print(f'got a post request! and request.json is: {request.json}')
		
		method=request.json["method"]
		part_number=request.json["product_pn"]
		free_sc_sn=[]
		for sn in dbq.get_free_sc_sn(part_number):
			free_sc_sn.append(sn["sc_sn"])
			
		if method=="FIFO":
			result=free_sc_sn[-1]

		if method=="LIFO":
			result=free_sc_sn[0]

		if method=="random":
			result=random.choice(free_sc_sn)


		print(f'free sc are: {free_sc_sn}')
		print(f'result is: {result}')
		return json.dumps({'sn':result}), 200, {'ContentType':'application/json'}


@webapp.route('/data/product_components_exist', methods=['GET', 'POST'])
@login_required
def get_product_components():
	# returns True if a product has Regular Compoenents otherwise returns False

	if request.method=="POST":
		
		print(f'got a post request! and request.json is: {request.json}')
		
		product_compoenents=dbq.get_db_product_components(request.json["product_sn"])

		if len(product_compoenents)==0:
			return json.dumps({'result':False}), 200, {'ContentType':'application/json'}

		else:
			return json.dumps({'result':True}), 200, {'ContentType':'application/json'}
	