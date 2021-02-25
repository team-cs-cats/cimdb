# filename: db_insert_queries
# description: provides INSERT database queries to add new data to each of the entity tables

# connect to databse
import cim.database.db_connector as db

# Create a connection to the database
db_connection = db.connect_to_database()


def insert(insert_query_to_run, data_to_insert):
	"""
	Since all insertion queries will share the same steps, 
	this is just a validation wrapper that handles whether an insertion was successful or not.
	"""
	
	# Attempt to insert. If successful, return True
	try:

		# Connect to the database. If we don't do this each time, MySQL Will Go Away
		db_connection = db.connect_to_database()

		# Execute the provided query using the provided data
		cursor = db.execute_query(db_connection=db_connection, query=insert_query_to_run, query_params=data_to_insert)
		return True
	
	# If unsuccessful, print the error to the server log and return False
	except Exception as e:
		print(f'An error occurred when attempting to insert into CIMDB: {str(e)}')
		return False


def insert_site(new_site_address_1, new_site_address_2, new_site_city, new_site_state, new_site_zip):

	# Load SQL query for INSERTing new site data
	add_site_query = """
	INSERT INTO Sites (site_address_1, site_address_2, site_address_city, site_address_state, site_address_postal_code)
	VALUES (%s, %s, %s, %s, %s);
	"""
	new_site_data = (new_site_address_1, new_site_address_2, new_site_city, new_site_state, new_site_zip)
	insert(insert_query_to_run=add_site_query, data_to_insert=new_site_data)


def insert_work_order(new_wo_open_date,new_wo_close_date, new_wo_status, new_wo_reference_number, new_wo_employee_id):

	# Load SQL query for INSERTing new work order data
	add_work_order_query = """
	INSERT INTO WorkOrders (wo_open_date, wo_close_date, wo_status, wo_reference_number, wo_employee_id)
	VALUES (%s, %s, %s, %s, %s);
	"""
	new_workorder_data=(new_wo_open_date,new_wo_close_date, new_wo_status, new_wo_reference_number, new_wo_employee_id)
	print(f'new work order data is: {new_workorder_data}')
	insert(insert_query_to_run=add_work_order_query,data_to_insert=new_workorder_data)


def insert_work_order_products(new_wop_wo_id,new_wop_product_sn):
	# Load SQL query for INSERTing new work order/products data

	add_work_order_products="""INSERT INTO WorkOrderProducts (wop_wo_id, wop_product_sn)
	VALUES (%s,%s);"""

	new_work_order_products_data=(new_wop_wo_id,new_wop_product_sn)
	insert(insert_query_to_run=add_work_order_products,data_to_insert=new_work_order_products_data)

	
	


def insert_employee(new_employee_group, new_employee_first_name, new_employee_last_name, 
	new_employee_email, new_employee_password, new_employee_site_id):

	# Load SQL query for INSERTing new employee data
	add_employee_query = """
	INSERT INTO Employees (employee_group, employee_first_name, employee_last_name, employee_email, employee_password, employee_site_id)
	VALUES (%s, %s, %s, %s, %s, %s);
	"""
	new_employee_data = (new_employee_group, new_employee_first_name, new_employee_last_name, 
		new_employee_email, new_employee_password, new_employee_site_id)
	insert(insert_query_to_run=add_employee_query, data_to_insert=new_employee_data)


def insert_location(new_location_room_number, new_location_shelf_number, new_location_site_id):

	# Load SQL query for INSERTing new location data
	add_location_query = """
	INSERT INTO Locations (location_room_number, location_shelf_number, location_site_id)
	VALUES (%s, %s, %s);
	"""
	new_location_data = (new_location_room_number, new_location_shelf_number, new_location_site_id)
	print('new_location_data', new_location_data)
	insert(insert_query_to_run=add_location_query, data_to_insert=new_location_data)


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


def insert_product(new_product_pn,new_product_family,new_product_date_assmebly,new_product_qc_date,
new_product_warranty_expiration_date,new_product_employee_id,new_product_location_id,new_product_sc_sn):

	# Load SQL query for INSERTing new product data
	add_product_query = """INSERT INTO Products (product_pn , product_family , product_date_assembly , product_qc_date,
product_warranty_expiration_date, product_employee_id, product_location_id, product_sc_sn )
VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
	"""
	new_product_data=(new_product_pn,new_product_family,new_product_date_assmebly,new_product_qc_date,
new_product_warranty_expiration_date,new_product_employee_id,new_product_location_id,new_product_sc_sn)
	insert(insert_query_to_run=add_product_query,data_to_insert=new_product_data)
	
	

def insert_regular_component():

	# Load SQL query for INSERTing new regular component data
	add_regular_component_query = """"""
	insert(insert_query_to_run=add_regular_component_query)

def insert_special_component():

	# Load SQL query for INSERTing new regular component data
	add_special_component_query = """"""
	insert(insert_query_to_run=add_special_component_query)

