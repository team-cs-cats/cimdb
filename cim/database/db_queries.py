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



def get_db_sites():
<<<<<<< HEAD
	# Load SQL query for site data
<<<<<<< HEAD
	query = "SELECT * FROM Sites;"
=======
	query = """SELECT * FROM Sites;"""
>>>>>>> upstream/main
=======
	# Load SQL query for site data (except for 'customer' site ie shipped products/work orders)
	query = """SELECT * FROM Sites
	WHERE site_id <> 1;"""
>>>>>>> upstream/main
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
	Sites.site_address_city as employee_site_name 
	FROM Employees 
	INNER JOIN Sites 
	ON Employees.employee_site_id=Sites.site_id;"""

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

	cursor = db.execute_query(db_connection=db_connection, query=query)
	work_order_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(work_order_results) == 0:
		work_order_results = data.get_wo()

	return work_order_results