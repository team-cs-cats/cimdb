# filename: db_queries
# description: provides simple database queries that are intended to be used repeatedly across multiple routes


# perform a local import to load the dummy data
from cim.dummy_data import DummyData

# connect to databse
import cim.database.db_connector as db


# Create a connection to the database
db_connection = db.connect_to_database()

# instantiate the dummy data in case database server data does not load properly
data = DummyData()


def get_site_id(city_name):

	# provided a site city name, return the site ID instead
	query = """SELECT site_id from Sites WHERE site_city_name == %s"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(city_name))
	site_id = cursor.fetchall()
	return site_id

def regular_component_locations(regular_component_id):

	# provided a regular component ID, return the locations of all regular components with that ID
	query = """
	SELECT 
	Locations.location_site_id AS location_site_id ,
	Locations.location_id AS location_id ,
	Locations.location_room_number AS location_room_number ,
	Locations.location_shelf_number AS location_shelf_number ,
	LocationsRegularComps.lrc_quantity AS quantity_at_location
	FROM Locations
	INNER JOIN LocationsRegularComps ON Locations.location_id=LocationsRegularComps.lrc_location_id
	WHERE LocationsRegularComps.lrc_rc_pn == %s;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query, query_params=(regular_component_id))
	reg_comp_location_results = cursor.fetchall()
	return reg_comp_location_results

# [
#       {"location_site_id": 12, "location_id": 50921, "location_room_number": 4, "location_shelf_number": 18, "quantity_at_location": 45},
#       {"location_site_id": 12, "location_id": 17815, "location_room_number": 8, "location_shelf_number": 2, "quantity_at_location": 23}, 
#       {"location_site_id": 12, "location_id": 37588, "location_room_number": 4, "location_shelf_number": 15, "quantity_at_location": 48}, 
#       {"location_site_id": 12, "location_id": 14369, "location_room_number": 3, "location_shelf_number": 2, "quantity_at_location": 12}
#     ]

def get_db_regular_components():

	# Load SQL query for regular component data
	query = """SELECT
	RegularComponents.rc_pn,
	RegularComponents.rc_pn_desc,
	RegularComponents.rc_category,
	SUM(LocationsRegularComps.lrc_quantity) AS TotalQuantity,
	Locations.location_room_number,
	Locations.location_shelf_number,
	Sites.site_address_city
	FROM RegularComponents 
	INNER JOIN LocationsRegularComps ON RegularComponents.rc_pn=LocationsRegularComps.lrc_rc_pn
	INNER JOIN Locations ON Locations.location_id=LocationsRegularComps.lrc_location_id
	INNER JOIN Sites ON Locations.location_site_id=Sites.site_id
    GROUP BY RegularComponents.rc_pn;
	"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	reg_comp_results = cursor.fetchall()
	return reg_comp_results


def get_db_special_components():

	# Load SQL query for regular component data
	query = """SELECT
	SpecialComponents.sc_sn AS sc_sn,
	SpecialComponents.sc_pn AS sc_pn,
	SpecialComponents.sc_is_free AS sc_free,
	SpecialComponents.sc_product_sn AS sc_product_sn,
	SpecialComponents.sc_location_id AS sc_loc_id,
	Locations.location_room_number AS sc_room,
	Locations.location_shelf_number AS sc_shelf,
	Sites.site_address_city AS sc_site_city
	FROM SpecialComponents 
	INNER JOIN Locations ON Locations.location_id=SpecialComponents.sc_location_id
	INNER JOIN Sites ON Locations.location_site_id=Sites.site_id
	"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	spec_comp_results = cursor.fetchall()
	return spec_comp_results


def get_db_regular_components_by_location():

	# Load SQL query for regular component data
	query = """SELECT
	LocationsRegularComps.lrc_rc_pn AS PartNumber,
	Sites.site_address_city AS SiteCity,
	Locations.location_room_number AS RoomNumber,
	Locations.location_shelf_number AS ShelfNumber,
	LocationsRegularComps.lrc_quantity AS Quantity
	FROM RegularComponents 
	INNER JOIN LocationsRegularComps ON RegularComponents.rc_pn=LocationsRegularComps.lrc_rc_pn
	INNER JOIN Locations ON Locations.location_id=LocationsRegularComps.lrc_location_id
	INNER JOIN Sites ON Locations.location_site_id=Sites.site_id
	ORDER BY SiteCity, Quantity DESC
	;
	"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	reg_comp_results = cursor.fetchall()
	return reg_comp_results



def get_db_sites():

	# Load SQL query for site data (except for 'customer' site ie shipped products/work orders)
	query = """SELECT * FROM Sites
	WHERE site_id <> 1;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	site_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(site_results) == 0:
		site_results = data.get_sites()

	return site_results


def get_db_locations():
	# Load SQL query for location data

	# select all columns from location table and site city name from site table
	# do not select sites or locations where 
	query = """SELECT 
	Locations.location_id, 
	Locations.location_room_number, 
	Locations.location_shelf_number, 
	Sites.site_address_city as location_site_name 
	FROM Locations 
	INNER JOIN Sites 
	ON Locations.location_site_id=Sites.site_id
	WHERE Locations.location_id <> 1 # ignore location 1 (shipped to customer)
	OR Sites.site_id <> 1 # ignore site 1 (shipped to customer)
	;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	location_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(location_results) == 0:
		location_results = data.get_loc()

	return location_results


def get_db_employees():
	# Load SQL query for employee data

	# select all columns except employee password from employee table, and site city name from site table
	query = """SELECT 
	Employees.employee_id, 
	Employees.employee_group, 
	Employees.employee_first_name, 
	Employees.employee_last_name, 
	Employees.employee_email, 
	Employees.employee_site_id,
	Sites.site_address_city AS employee_site_name 
	FROM Employees 
	INNER JOIN Sites 
	ON Employees.employee_site_id=Sites.site_id;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	employee_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(employee_results) == 0:
		employee_results = data.get_emp()

	return employee_results


def get_db_work_orders():
	# Load SQL query for work order data

	# select all columns except employee password from employee table, and site city name from site table
	query = """SELECT 
	WorkOrders.wo_id, 
	WorkOrders.wo_open_date, 
	WorkOrders.wo_close_date, 
	WorkOrders.wo_status, 
	WorkOrders.wo_reference_number,
	CONCAT(Employees.employee_first_name, ' ', Employees.employee_last_name) as wo_employee_full_name 
	FROM WorkOrders 
	INNER JOIN Employees 
	ON Employees.employee_id=WorkOrders.wo_employee_id;"""

	#TODO: also get the work order details (products involved)
	
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	work_order_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(work_order_results) == 0:
		work_order_results = data.get_wo()

	return work_order_results


def get_a_work_order(workorder_id):
	# returns a sinlge worker information

	query = """SELECT 
	WorkOrders.wo_id, 
	WorkOrders.wo_open_date, 
	WorkOrders.wo_close_date, 
	WorkOrders.wo_status, 
	WorkOrders.wo_reference_number,
	WorkOrders.wo_employee_id,
	CONCAT(Employees.employee_first_name, ' ', Employees.employee_last_name) as wo_employee_full_name 
	FROM WorkOrders 
	INNER JOIN Employees 
	ON Employees.employee_id=WorkOrders.wo_employee_id
	where WorkOrders.wo_id="""+workorder_id+""";"""
		
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	work_order_result = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	# if len(work_order_result) == 0:
	# 	work_order_result = data.get_wo()

	return work_order_result[0]


def get_db_workorder_details(workorder_id):
	# Load SQL query for work order details

	query = """select * from Products inner join
	WorkOrderProducts on WorkOrderProducts.wop_product_sn=Products.product_sn
	where WorkOrderProducts.wop_wo_id="""+workorder_id+""";"""

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	workorder_details_result = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	# if len(workorder_details_result) == 0:
	# 	workorder_details_result = data.get_wo()

	return workorder_details_result


def get_free_sc_sn(sc_pn):
	# returns SN of the free special compoenents of a family
	query = """select sc_sn from SpecialComponents 
	where sc_is_free=1 AND sc_pn='"""+sc_pn+"""' ORDER BY sc_sn DESC;"""

	print(f'querry is {query}')

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	free_sc_sn_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(free_sc_sn_results) == 0:
		print("EROOR in FREE SC!!!")

	return free_sc_sn_results


def get_product_sn(sc_sn):
	# returns SN of the product using its SC SN, if SC is not used, returns False

	# if get_is_free(sc_sn) is True:
	# 	return False

	query = """select product_sn from Products 
	where product_sc_sn="""+str(sc_sn)+""";"""
	
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	get_product_sn_result = cursor.fetchall()

	# print(f'get_product_sn_result is: {get_product_sn_result[0]["product_sn"]}')

	if len(get_product_sn_result) == 0:
		return -1
	
	else:
		return get_product_sn_result[0]["product_sn"]
	

def update_is_free(sc_sn):
	# should be added to upate queries later
	# updates is_free attr of a SC once it's assigned to a product

	query = """UPDATE SpecialComponents SET sc_is_free=0 WHERE sc_sn ="""+str(sc_sn)+""" ;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	
	
def get_is_free(sc_sn):
	# returns True if a SC is free otherwise flase
	query = """select sc_is_free from SpecialComponents 
	where sc_sn="""+str(sc_sn)+""";"""

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	is_free_result = cursor.fetchall()
	# print(f'is_free_result is: {is_free_result[0]["sc_is_free"]}')

	if is_free_result[0]["sc_is_free"]==1:
		return True
	
	else:
		return False


def rev_update_is_free(sc_sn):
	# will be deleted--- only for dev purposes
	
	query = """UPDATE SpecialComponents SET sc_is_free=1 WHERE sc_sn ="""+str(sc_sn)+""" ;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)

	
def get_assembly_list(employee_id=None):
	# returns itmes in the assmebly line for a given employee. if id is None, it returns all items (for admins)

	if employee_id is None:
		query="""select WorkOrders.wo_id, WorkOrders.wo_open_date , Products.product_sn,
		Products.product_family, Products.product_pn from WorkOrders
		inner join WorkOrderProducts on WorkOrders.wo_id=WorkOrderProducts.wop_wo_id
		inner join Products on Products.product_sn = WorkOrderProducts.wop_product_sn
		where Products.product_qc_date is Null and Products.product_date_assembly is not Null;"""
	else:
		query='''select WorkOrders.wo_id, WorkOrders.wo_open_date , Products.product_sn,
		Products.product_family, Products.product_pn from WorkOrders
		inner join WorkOrderProducts on WorkOrders.wo_id=WorkOrderProducts.wop_wo_id
		inner join Products on Products.product_sn = WorkOrderProducts.wop_product_sn
		where WorkOrders.wo_employee_id='''+str(employee_id)+''' and Products.product_qc_date is Null and Products.product_date_assembly is not Null;'''

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	assmebly_line_results=cursor.fetchall()

	return assmebly_line_results


def get_qc_list(employee_id=None):
	# returns itmes in the qc line for a given employee. if id is None, it returns all items (for admins)

	if employee_id is None:
		query="""select WorkOrders.wo_id, WorkOrders.wo_open_date , Products.product_sn,
		Products.product_family, Products.product_pn from WorkOrders
		inner join WorkOrderProducts on WorkOrders.wo_id=WorkOrderProducts.wop_wo_id
		inner join Products on Products.product_sn = WorkOrderProducts.wop_product_sn
		where Products.product_qc_date is not Null and Products.product_date_assembly is not Null 
		and Products.product_warranty_expiration_date is Null;"""
	else:
		query='''select WorkOrders.wo_id, WorkOrders.wo_open_date , Products.product_sn,
		Products.product_family, Products.product_pn from WorkOrders
		inner join WorkOrderProducts on WorkOrders.wo_id=WorkOrderProducts.wop_wo_id
		inner join Products on Products.product_sn = WorkOrderProducts.wop_product_sn
		where WorkOrders.wo_employee_id='''+str(employee_id)+''' and Products.product_qc_date is not Null and
		Products.product_date_assembly is not Null and Products.product_warranty_expiration_date is Null;'''

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	assmebly_line_results=cursor.fetchall()

	return assmebly_line_results


def get_db_product_details(product_sn):
	
	# returns a product infroamtion based on it's SN. returns an empty dictionary if the sn does not exists

	query = """SELECT
	Products.product_sn , Products.product_pn , Products.product_family , Products.product_date_assembly ,
	Products.product_qc_date,Products.product_warranty_expiration_date, Products.product_employee_id,
	Products.product_location_id, Products.product_sc_sn,
	CONCAT(Employees.employee_first_name, ' ', Employees.employee_last_name) as product_employee_full_name 
	FROM Products 
	INNER JOIN Employees 
	ON Employees.employee_id=Products.product_employee_id
	where Products.product_sn="""+str(product_sn)+""";"""
		
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	product_result = cursor.fetchall()

	if len(product_result) == 0:
		return {}
	
	return product_result[0]


def get_db_product_components(product_sn):

	# returns products compoenent based on it's SN. returns an empty dictionary if the sn does not exists

	if len(get_db_product_details(product_sn)) == 0:
		print("product is not found") 
		product_compoenent_result={}
	
	else:
		query = """select ProductsRegularComps.prc_rc_pn , ProductsRegularComps.prc_quantity_needed,
		RegularComponents.rc_pn_desc , RegularComponents.rc_category
		FROM ProductsRegularComps inner join RegularComponents on 
		ProductsRegularComps.prc_rc_pn = RegularComponents.rc_pn 
		where ProductsRegularComps.prc_product_sn="""+str(product_sn)+""";"""
		
		db_connection = db.connect_to_database()
		cursor = db.execute_query(db_connection=db_connection, query=query)
		product_compoenent_result = cursor.fetchall()
	
		
	return list(product_compoenent_result)

def get_db_regular_component_desc(rc_pn):
	# returns a regular compoenent desc of a given rc_pn
	
	query = """select RegularComponents.rc_pn_desc from RegularComponents where
	RegularComponents.rc_pn="""+str(rc_pn)+""";"""
		
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	regular_component_desc_result = cursor.fetchall()
	
		
	return regular_component_desc_result

def get_db_regular_component_pn(rc_pn_desc):
	# returns a regular compoenent part number of a given rc_pn_desc
	
	query = """select RegularComponents.rc_pn from RegularComponents where
	RegularComponents.rc_pn_desc='"""+rc_pn_desc+"""';"""
		
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	regular_component_pn_result = cursor.fetchall()
	
		
	return regular_component_pn_result



def get_newest_regular_component_part_number():
	# returns the most recently added regular component part number from the regular components entity

	query = """SELECT rc_pn FROM RegularComponents WHERE rc_pn=(SELECT max(rc_pn) FROM RegularComponents);"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)
	regular_component_pn_result = cursor.fetchall()
	return regular_component_pn_result[0]['rc_pn']