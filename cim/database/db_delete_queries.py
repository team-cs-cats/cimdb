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
	
	# Attempt to delete. If successful, return True
	try:
		db_connection = db.connect_to_database()
		cursor = db.execute_query(db_connection=db_connection, query=delete_query_to_run)
		return True
	
	# If unsuccessful, print the error to the server log and return False
	except Exception as e:
		print(f'An error occurred when attempting to delete from CIMDB: {str(e)}')
		return False


def delete_site(site_id_to_delete):

	# Load SQL query for DELETEing the data for a selected site 
	delete_site_query = """
	DELETE FROM Sites WHERE site_id='%s';
	"""%(site_id_to_delete)
	delete(delete_query_to_run=delete_site_query)


def delete_work_order(wo_id):

	# Load SQL query for DELETEing the data for a selected work order 
	delete_work_order_query = """DELETE FROM WorkOrders WHERE wo_id="""+wo_id+""" ;"""
	delete(delete_query_to_run=delete_work_order_query)


def delete_work_order_products_by_wo_id(wo_id):

	# Load SQL query for DELETEing the data for a selected work order/products 
	delete_work_order_products_by_wo_id_query = """DELETE FROM WorkOrderProducts WHERE wop_wo_id="""+wo_id+""" ;"""
	delete(delete_query_to_run=delete_work_order_products_by_wo_id_query)

def delete_work_order_products_by_product_sn(product_sn):

	# Load SQL query for DELETEing the data for a selected work order/products 
	delete_work_order_products_by_wo_id_query = """DELETE FROM WorkOrderProducts WHERE wop_product_sn="""+product_sn+""" ;"""
	delete(delete_query_to_run=delete_work_order_products_by_wo_id_query)

def delete_employee(employee_id_to_delete):

	# Load SQL query for DELETEing the data for a selected employee 
	delete_employee_query = """
	DELETE FROM Employees WHERE employee_id='%s';
	"""%(employee_id_to_delete)
	delete(delete_query_to_run=delete_employee_query)


def delete_location(location_id_to_delete):

	# Load SQL query for DELETEing the data for a selected location
	delete_location_query = """
	DELETE FROM Locations WHERE location_id='%s';
	"""%(location_id_to_delete)
	delete(delete_query_to_run=delete_location_query)


def delete_location_regular_comps():

	# Load SQL query for DELETEing the data for a selected locations/regular components relationship
	delete_location_regular_comps_query = """"""
	delete(delete_query_to_run=delete_location_regular_comps_query)


def delete_products_regular_comps(product_sn):

	# Load SQL query for DELETEing the data for a selected products/regular components relationship
	delete_product_regular_comps_query = """DELETE FROM ProductsRegularComps WHERE prc_product_sn = """+product_sn+""" ;"""
	delete(delete_query_to_run=delete_product_regular_comps_query)


def delete_products_special_comps():

	# Load SQL query for DELETEing the data for a selected products/special components relationship
	delete_product_special_comps_query = """"""
	delete(delete_query_to_run=delete_product_special_comps_query)


def delete_product(product_sn):

	# Load SQL query for DELETEing the data for a selected product
	delete_product_query = """DELETE FROM Products WHERE product_sn = """+product_sn+""" ;"""
	delete(delete_query_to_run=delete_product_query)


def delete_regular_component():

	# Load SQL query for DELETEing the data for a selected regular component
	delete_regular_component_query = """"""
	delete(delete_query_to_run=delete_regular_component_query)

def delete_special_component(spec_comp_sn_to_delete):

	# Load SQL query for DELETEing the data for a selected regular component
	delete_special_component_query = """
	DELETE FROM SpecialComponents WHERE sc_sn='%s';
	"""%(spec_comp_sn_to_delete)
	delete(delete_query_to_run=delete_special_component_query)
