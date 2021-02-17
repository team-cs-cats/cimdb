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
	# Load SQL query for site data
	query = """SELECT * FROM Sites;"""
	cursor = db.execute_query(db_connection=db_connection, query=query)
	site_results = cursor.fetchall()

	# Check if the query was successful: if it returned content we are good. If not, use the dummy dataset instead.
	if len(site_results) == 0:
		site_results = data.get_sites()

	return site_results


def get_db_locations():
	# Load SQL query for location data

	# select all columns from location table and site city name from site table
	query = """SELECT 
	Locations.location_id, 
	Locations.location_room_number, 
	Locations.location_shelf_number, 
	Sites.site_address_city as location_site_name 
	FROM Locations 
	INNER JOIN Sites 
	ON Locations.location_site_id=Sites.site_id;"""

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