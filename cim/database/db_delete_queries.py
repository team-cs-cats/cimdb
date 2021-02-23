# filename: db_delete_queries
# description: provides DELETE database queries to delete selected data from each of the entity tables

# connect to database
import cim.database.db_connector as db

# Create a connection to the database
db_connection = db.connect_to_database()


def delete(delete_query_to_run):
	"""
	Since all deletion queries will share the same steps, 
	this is just a validation wrapper that handles whether a delete was successful or not.
	"""
	
	# Attempt to insert. If successful, return True
	try:
		cursor = db.execute_query(db_connection=db_connection, query=query_to_run)
		return True
	
	# If unsuccessful, print the error to the server log and return False
	except Exception as e:
		print(f'An error occurred when attempting to delete from CIMDB: {str(e)}')
		return False


def delete_site():

	# Load SQL query for DELETEing the data for a selected site 
	delete_site_query = """"""
	delete(delete_query_to_run=delete_site_query)


def delete_work_order():

	# Load SQL query for DELETEing the data for a selected work order 
	delete_work_order_query = """"""
	delete(delete_query_to_run=delete_work_order_query)


def delete_work_order_products():

	# Load SQL query for DELETEing the data for a selected work order/products 
	delete_work_order_products_query = """"""
	delete(delete_query_to_run=delete_work_order_products_query)


def delete_employee():

	# Load SQL query for DELETEing the data for a selected employee 
	delete_employee_query = """"""
	delete(delete_query_to_run=delete_employee_query)


def delete_location():

	# Load SQL query for DELETEing the data for a selected location
	delete_location_query = """"""
	delete(delete_query_to_run=delete_location_query)


def delete_location_regular_comps():

	# Load SQL query for DELETEing the data for a selected locations/regular components relationship
	delete_location_regular_comps_query = """"""
	delete(delete_query_to_run=delete_location_regular_comps_query)


def delete_products_regular_comps():

	# Load SQL query for DELETEing the data for a selected products/regular components relationship
	delete_product_regular_comps_query = """"""
	delete(delete_query_to_run=delete_product_regular_comps_query)


def delete_products_special_comps():

	# Load SQL query for DELETEing the data for a selected products/special components relationship
	delete_product_special_comps_query = """"""
	delete(delete_query_to_run=delete_product_special_comps_query)


def delete_product():

	# Load SQL query for DELETEing the data for a selected product
	delete_product_query = """"""
	delete(delete_query_to_run=delete_product_query)


def delete_regular_component():

	# Load SQL query for DELETEing the data for a selected regular component
	delete_regular_component_query = """"""
	delete(delete_query_to_run=delete_regular_component_query)

def delete_special_component():

	# Load SQL query for DELETEing the data for a selected regular component
	delete_special_component_query = """"""
	delete(delete_query_to_run=delete_special_component_query)
