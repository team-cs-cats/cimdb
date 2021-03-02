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
		db_connection = db.connect_to_database()
		cursor = db.execute_query(db_connection=db_connection, query=update_query_to_run)
		return True
	
	# If unsuccessful, print the error to the server log and return False
	except Exception as e:
		print(f'An error occurred when attempting to update an existing record on CIMDB: {str(e)}')
		return False


def update_site(update_site_address_1, update_site_address_2, update_site_city, update_site_state, update_site_zip, site_id_to_update):

	# Load SQL query for updating the data for a selected site 
	update_site_query = """
	UPDATE Sites SET 
	site_address_1 = '%s', 
	site_address_2 = '%s', 
	site_address_city = '%s', 
	site_address_state = '%s', 
	site_address_postal_code = %s
	WHERE site_id = %s
	;
	""" % (update_site_address_1, update_site_address_2, update_site_city, update_site_state, update_site_zip, site_id_to_update)
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

def update_special_component(updated_spec_comp_part_number,
					updated_spec_comp_location,
					updated_spec_comp_is_free,
					sc_id_to_update):

	# # First, use the provided Site city and Location room number and shelf number to obtain a new location id where the special component should be moved to
	# new_location_query = """
	# SELECT location_id
	# FROM Locations
	# INNER JOIN Sites ON Locations.location_site_id = Sites.site_id
	# WHERE Sites.site_address_city = '%s' 
	# AND Locations.location_room_number = '%s'
	# AND Locations.location_shelf_number = '%s'
	# LIMIT 1
	# """
	# db_connection = db.connect_to_database()
	# params = (updated_spec_comp_site, updated_spec_comp_room_number, updated_spec_comp_shelf_number, )
	# cursor = db.execute_query(db_connection=db_connection, query=new_location_query, query_params=params)
	# location_id_results = cursor.fetchall()

	# print('location_id_results:', location_id_results)

	# # check if there are no results (ie, the special component was moved to a non-existent location)
	# if len(location_id_results) == 0:
	# 	print('~~~~~~~~~~ No location exists with these details')

	# new_location_id = location_id_results[0]['location_id']




	# Load SQL query for updating the data for a selected regular component
	update_special_component_query = """
	UPDATE SpecialComponents SET 
	sc_pn = '%s',
	sc_is_free = '%s',
	sc_location_id = '%s'
	WHERE sc_sn = %s
	;
	""" % (updated_spec_comp_part_number, updated_spec_comp_is_free, updated_spec_comp_location, sc_id_to_update)
	update(update_query_to_run=update_special_component_query)


	# TODO: add special_component / product number functionality


def update_site(update_site_address_1, update_site_address_2, update_site_city, update_site_state, update_site_zip, site_id_to_update):

	# Load SQL query for updating the data for a selected site 
	update_site_query = """
	UPDATE Sites SET 
	site_address_1 = '%s', 
	site_address_2 = '%s', 
	site_address_city = '%s', 
	site_address_state = '%s', 
	site_address_postal_code = %s
	WHERE site_id = %s
	;
	""" % (update_site_address_1, update_site_address_2, update_site_city, update_site_state, update_site_zip, site_id_to_update)
	update(update_query_to_run=update_site_query)