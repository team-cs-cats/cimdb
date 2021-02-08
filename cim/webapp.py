# webapp.py
from flask import Flask, render_template
from flask import request, redirect

# import these to handle user accounts
from flask import url_for, session
import flask_login
from flask_login import login_user, current_user, logout_user, login_required


# perform a local import to load the dummy data
from cim.dummy_data import DummyData

# This will eventually connect to the database, but for now it is not enabled
# from db_connector.db_connector import connect_to_database, execute_query


#create the web application
webapp = Flask(__name__)

# added a 'secret' key for user management
webapp.secret_key = 'Team CS Cats'


# Set up login manager to handle basic user authentication
login_manager = flask_login.LoginManager()
login_manager.init_app(webapp)





# Load dummy data for the webpages to reference
data = DummyData()


# Set up a mock set of user ids to use for our logins (this can be moved/replaced later)
users = {}

for employee in data.get_emp():
    emp_email = employee["employee_email"]
    emp_pass = employee["employee_password"]
    users[emp_email] = {'password': emp_pass}


print(users)


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

# # Associate a logged in user with the current session
# @login_manager.request_loader
# def request_loader(request):

# 	# obtain the current email
#     email = request.form.get('email')

#     # if the current email isn't on the list of allowed users, return nothing
#     if email not in users:
#         return

#     # if the user email is allowed, set it as the id of the current user
#     user = User()
#     user.id = email
#     user.is_authenticated = request.form['password'] == users[email]['password']
#     return user

# # Add an association for any unauthorized session logins.
# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized'




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
        current_employee_id = None
        for employee_info in data.get_emp():
            if employee_info['employee_email'] == email:
                current_employee_id = employee_info['employee_id']
                break

        # if we couldn't find the employee id, redirect to the index
        if current_employee_id is None:
            return redirect(url_for('index'))

        # otherwise save the id and render the landing page
        user.employee_id = current_employee_id
        flask_login.login_user(user)
        return redirect(url_for('landing', current_employee_id=user.employee_id))

    # If the user provided bad credentials, return them to the index page (TODO: flash error)
    return render_template("index.html")


# Provide a route to log out the web app
@webapp.route('/logout', methods=['GET', 'POST'])
def logout():
    flask_login.logout_user()
    return render_template("index.html")


@webapp.route('/workorders', methods=['GET', 'POST'])
@login_required
def workorders():
    """The webapp's page for work orders, which allows reviewing and adding work orders."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
    	return redirect(url_for("cim.templates.index"))

    # otherwise, return the workorders page
    if request.method=="GET":
        return render_template("workorders.html")

@webapp.route('/landing', methods=['GET', 'POST'])
@login_required
def landing():
    """The webapp's logged in landing page, which allows an employee to access the internal links."""

    # otherwise, return the landing page and pass it the employee ID which can be used as a key
    if request.method=="GET":
        return render_template("landing.html", current_emp_id=request.args.get('current_employee_id'))

@webapp.route('/products', methods=['GET', 'POST'])
@login_required
def products():
    """The webapp's page for viewing an employee's currently assigned products to assemble and QC."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
        return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        return render_template("products.html")

@webapp.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventory():
    """The webapp's page for viewing the inventory.
    This allows the employee to review existing stock and order new stock of standard and special components."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
        return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        return render_template("inventory.html", regular_components=data.get_rc(), special_components=data.get_sc(), sites=data.get_sites())

@webapp.route('/shipping', methods=['GET', 'POST'])
@login_required
def shipping():
    """The webapp's page for viewing the shipping status of work orders.
    This allows the employee to review existing work orders and see if they are ready to ship or not."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
        return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        return render_template("shipping.html", work_orders=data.get_wo(), employees=data.get_emp())

@webapp.route('/locations', methods=['GET', 'POST'])
@login_required
def locations():
    """The webapp's page for viewing the locations at the various sites, 
    as well as which regular components, special components, and products are placed in which locations."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
        return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        return render_template("locations.html", 
        locations=data.get_loc(), products=data.get_products(), regular_components=data.get_rc(), special_components=data.get_sc(), sites=data.get_sites())

@webapp.route('/management', methods=['GET', 'POST'])
@login_required
def user_management():
    """The webapp's page for managing current users.
    This allows a manager to update information about current users."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
        return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        return render_template("user_management.html", sites=data.get_sites(), employees=data.get_emp())

# workorder details. it takes the wo_id as argument to retrive the the information from DB
@webapp.route('/wo-details', methods=['GET', 'POST'])
@login_required
def wo_details(wo_id=None):
    """The webapp's page takes wo_id and retirve the inforamtion from DB."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
    	return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        
        #if wo_id not none:
            #SQL query
        # render the detail page
        return render_template("wo-details.html")


# products details. it takes the product_sn as argument to retrive the the information from DB
@webapp.route('/product-details', methods=['GET', 'POST'])
@login_required
def product_details(product_sn=None):
    """The webapp's page takes product_sn and retirve the inforamtion from DB."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
    	return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        
        #if product_sn not none:
            #SQL query
        # render the detail page
        return render_template("product-details.html")

# Assembly page. The page lists are assigned products ready for assembly 
@webapp.route('/assembly', methods=['GET', 'POST'])
@login_required
def assembly():
    """The webapp's page retirve the inforamtion from DB for the Assembly process."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
    	return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        
        #SQL query

        # render the assembly page
        return render_template("assembly.html")


# QC page. The page lists are assigned products ready for assembly 
@webapp.route('/qc', methods=['GET', 'POST'])
@login_required
def QC():
    """The webapp's page retirve the inforamtion from DB for the Assembly process."""

    # if the current user is not authenticated, redirect the user to the logged out index page
    if not current_user.is_authenticated:
    	return redirect(url_for("cim.templates.index"))

    if request.method=="GET":
        
        #SQL query

        # render the assembly page
        return render_template("qc.html")