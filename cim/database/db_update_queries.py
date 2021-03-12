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


def update_work_order(wo_id,update_wo_open_date,update_wo_close_date,update_wo_status,update_wo_reference_number,update_wo_employee_id):

	# Load SQL query for updating the data for a selected work order 
	# update_work_order_query = """UPDATE WorkOrders SET
	# wo_open_date = '"""+str(update_wo_open_date)+"""', 
	# wo_close_date = '"""+update_wo_close_date+"""', 
	# wo_status = '"""+update_wo_status+"""', 
	# wo_reference_number = """+str(update_wo_reference_number)+""", 
	# wo_employee_id = """+str(update_wo_employee_id)+""" 
	# WHERE wo_id = """+str(wo_id)+""" ;""" 

	update_work_order_query = """UPDATE WorkOrders SET
	wo_open_date = %s, 
	wo_close_date = %s, 
	wo_status = %s, 
	wo_reference_number = %s, 
	wo_employee_id = %s 
	WHERE wo_id = %s ;"""	%(update_wo_open_date,update_wo_close_date,update_wo_status,update_wo_reference_number,update_wo_employee_id,wo_id)
	
	# print("update_work_order_query is: ",update_work_order_query)
	update(update_query_to_run=update_work_order_query)
	


def update_work_order_products():

	# Load SQL query for updating the data for a selected work order/products 
	update_work_order_products_query = """"""
	update(update_query_to_run=update_work_order_products_query)


def update_employee(employee_group_input, employee_first_name_input, employee_last_name_input, 
	employee_email_input, employee_site_id_dropdown_input, employee_id_from_update_button):

	# Load SQL query for updating the data for a selected employee 
	update_employee_query = """
	UPDATE Employees SET 
	employee_group = '%s',
	employee_first_name = '%s',
	employee_last_name = '%s',
	employee_email = '%s',
	employee_site_id = '%s'
	WHERE employee_id = '%s';
	;
	""" % (employee_group_input, employee_first_name_input, employee_last_name_input, 
		employee_email_input, employee_site_id_dropdown_input, employee_id_from_update_button)
	update(update_query_to_run=update_employee_query)


def update_location(location_room_number_input, location_shelf_number_input, 
	location_site_id_dropdown_input, location_id_from_update_button):

	# Load SQL query for updating the data for a selected location
	update_location_query = """
		UPDATE Locations SET 
		 location_room_number = '%s',
		 location_shelf_number = '%s',
		 location_site_id = '%s'
		WHERE location_id = '%s';
	""" % (location_room_number_input, location_shelf_number_input, 
	location_site_id_dropdown_input, location_id_from_update_button)
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


def update_product(update_product_pn,update_product_family,update_product_date_assembly,
update_product_qc_date,update_product_warranty_expiration_date,update_product_location_id,product_sn):

	# Load SQL query for updating the data for a selected product
	update_product_query = """UPDATE Products SET
	product_pn = %s,
	product_family= %s,
	product_date_assembly=%s,
	product_qc_date = %s,
	product_warranty_expiration_date = %s,
	product_location_id=%s
	WHERE product_sn = %s""" %(update_product_pn,update_product_family,update_product_date_assembly,
	update_product_qc_date,update_product_warranty_expiration_date,update_product_location_id,product_sn)

	update(update_query_to_run=update_product_query)


def update_regular_component():

	# Load SQL query for updating the data for a selected regular component
	update_regular_component_query = """"""
	update(update_query_to_run=update_regular_component_query)

def update_special_component(updated_spec_comp_part_number,
					updated_spec_comp_location,
					updated_spec_comp_is_free,
					sc_id_to_update):

	# Load SQL query for updating the data for a selected regular component
	update_special_component_query = """
	UPDATE SpecialComponents SET 
	sc_pn = '%s',
	sc_is_free = '%s',
	sc_location_id = '%s'
	WHERE sc_sn = '%s';
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

#partial updates. these functions are used to update a sinlge attr of an entity

def set_sc_not_free(sc_sn):
	#  updates is_free attr of a SC once it's assigned to a product

	query = """UPDATE SpecialComponents SET sc_is_free=0 WHERE sc_sn ="""+str(sc_sn)+""" ;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)

def set_sc_free(sc_sn):
	
	
	query = """UPDATE SpecialComponents SET sc_is_free=1 WHERE sc_sn ="""+str(sc_sn)+""" ;"""
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)


def set_sc_location(sc_sn,sc_location_id):
	# updates location of a SC

	query = """UPDATE SpecialComponents SET
	sc_location_id= """+sc_location_id+""" WHERE sc_sn ="""+str(sc_sn)+""" ;"""

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query) 


def set_rc_qunatity_in_a_location(rc_pn,sc_location_id,quantity):
	# updates quantity of a location

	query = """UPDATE LocationsRegularComps SET
	lrc_quantity= """+quantity+""" WHERE lrc_location_id ="""+sc_location_id+"""
	AND lrc_rc_pn= """+rc_pn+""" ;"""

	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)

def set_sc_sn_of_a_product(sc_sn,product_sn):
	# updates sc_sn of a product

	query = """UPDATE Products SET
	product_sc_sn= """+sc_sn+""" WHERE product_sn ="""+product_sn+""" ;"""
	
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)


def set_product_qc_date(product_sn,product_qc_date):
	# updates product_qc_date of a product. used for QC approval

	query = """UPDATE Products SET
	product_qc_date= """+product_qc_date+""" WHERE product_sn ="""+product_sn+""" ;"""
	
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)

def set_product_date_assembly(product_sn,product_date_assembly):
	# updates product_date_assembly of a product. used for assembly approval

	query = """UPDATE Products SET
	product_date_assembly= """+product_date_assembly+""" WHERE product_sn ="""+product_sn+""" ;"""
	
	db_connection = db.connect_to_database()
	cursor = db.execute_query(db_connection=db_connection, query=query)

