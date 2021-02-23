# filename: db_update_queries
# description: provides update database queries to update selected data on each of the entity tables

# connect to database
import cim.database.db_connector as db

# Create a connection to the database
db_connection = db.connect_to_database()


def update(update_query_to_run):
	"""
	Since all update queries will share the same steps, 
	this is just a validation wrapper that handles whether an update was successful or not.
	"""
	
	# Attempt to update. If successful, return True
	try:
		cursor = db.execute_query(db_connection=db_connection, query=query_to_run)
		return True
	
	# If unsuccessful, print the error to the server log and return False
	except Exception as e:
		print(f'An error occurred when attempting to update an existing record on CIMDB: {str(e)}')
		return False


def update_site():

	# Load SQL query for updating the data for a selected site 
	update_site_query = """"""
	update(update_query_to_run=update_site_query)


def update_work_order():

	# Load SQL query for updating the data for a selected work order 
	update_work_order_query = """"""
	update(update_query_to_run=update_work_order_query)


def update_work_order_products():

	# Load SQL query for updating the data for a selected work order/products 
	update_work_order_products_query = """"""
	update(update_query_to_run=update_work_order_products_query)


def update_employee():

	# Load SQL query for updating the data for a selected employee 
	update_employee_query = """"""
	update(update_query_to_run=update_employee_query)


def update_location():

	# Load SQL query for updating the data for a selected location
	update_location_query = """"""
	update(update_query_to_run=update_location_query)


def update_location_regular_comps():

	# Load SQL query for updating the data for a selected locations/regular components relationship
	update_location_regular_comps_query = """"""
	update(update_query_to_run=update_location_regular_comps_query)


def update_products_regular_comps():

	# Load SQL query for updating the data for a selected products/regular components relationship
	update_product_regular_comps_query = """"""
	update(update_query_to_run=update_product_regular_comps_query)


def update_products_special_comps():

	# Load SQL query for updating the data for a selected products/special components relationship
	update_product_special_comps_query = """"""
	update(update_query_to_run=update_product_special_comps_query)


def update_product():

	# Load SQL query for updating the data for a selected product
	update_product_query = """"""
	update(update_query_to_run=update_product_query)


def update_regular_component():

	# Load SQL query for updating the data for a selected regular component
	update_regular_component_query = """"""
	update(update_query_to_run=update_regular_component_query)

def update_special_component():

	# Load SQL query for updating the data for a selected regular component
	update_special_component_query = """"""
	update(update_query_to_run=update_special_component_query)
