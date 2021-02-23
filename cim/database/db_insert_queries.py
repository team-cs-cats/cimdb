# filename: db_insert_queries
# description: provides INSERT database queries to add new data to each of the entity tables

# connect to databse
import cim.database.db_connector as db

# Create a connection to the database
db_connection = db.connect_to_database()


def insert(insert_query_to_run):
	"""
	Since all insertion queries will share the same steps, 
	this is just a validation wrapper that handles whether an insertion was successful or not.
	"""
	
	# Attempt to insert. If successful, return True
	try:
		cursor = db.execute_query(db_connection=db_connection, query=query_to_run)
		return True
	
	# If unsuccessful, print the error to the server log and return False
	except Exception as e:
		print(f'An error occurred when attempting to insert into CIMDB: {str(e)}')
		return False


def insert_site():

	# Load SQL query for INSERTing new site data
	add_site_query = """"""
	insert(insert_query_to_run=add_site_query)


def insert_work_order():

	# Load SQL query for INSERTing new work order data
	add_work_order_query = """"""
	insert(insert_query_to_run=add_work_order_query)


def insert_work_order_products():

	# Load SQL query for INSERTing new work order/products data
	add_work_order_products_query = """"""
	insert(insert_query_to_run=add_work_order_products_query)


def insert_employee():

	# Load SQL query for INSERTing new employee data
	add_employee_query = """"""
	insert(insert_query_to_run=add_employee_query)


def insert_location():

	# Load SQL query for INSERTing new location data
	add_location_query = """"""
	insert(insert_query_to_run=add_location_query)


def insert_location_regular_comps():

	# Load SQL query for INSERTing new locations/regular components data
	add_location_regular_comps_query = """"""
	insert(insert_query_to_run=add_location_regular_comps_query)


def insert_products_regular_comps():

	# Load SQL query for INSERTing new products/regular components data
	add_product_regular_comps_query = """"""
	insert(insert_query_to_run=add_product_regular_comps_query)


def insert_products_special_comps():

	# Load SQL query for INSERTing new products/special components data
	add_product_special_comps_query = """"""
	insert(insert_query_to_run=add_product_special_comps_query)


def insert_product():

	# Load SQL query for INSERTing new product data
	add_product_query = """"""
	insert(insert_query_to_run=add_product_query)


def insert_regular_component():

	# Load SQL query for INSERTing new regular component data
	add_regular_component_query = """"""
	insert(insert_query_to_run=add_regular_component_query)

def insert_special_component():

	# Load SQL query for INSERTing new regular component data
	add_special_component_query = """"""
	insert(insert_query_to_run=add_special_component_query)
