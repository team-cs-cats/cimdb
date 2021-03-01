# filename: db_filter_queries
# description: provides filter database queries to add filter data to each of the entity tables

# connect to databse
import cim.database.db_connector as db

# Create a connection to the database
db_connection = db.connect_to_database()



def filter(filter_query_to_run, data_to_filter):
    """
    Since all filter queries will share the same steps, 
    this is just a validation wrapper that handles whether an filterion was successful or not.
    """
    
    # Attempt to filter. If successful, return True
    try:

        # Connect to the database. If we don't do this each time, MySQL Will Go Away
        db_connection = db.connect_to_database()

        # Execute the provided query using the provided data
        cursor = db.execute_query(db_connection=db_connection, query=filter_query_to_run, query_params=data_to_filter)
        return True

    # If unsuccessful, print the error to the server log and return False
    except Exception as e:
        print(f'An error occurred when attempting to filter into CIMDB: {str(e)}')
        return False



def get_filtered_regular_components(filtered_terms):

    filter_query = """
    SELECT 
    RegularComponents.rc_pn,
    RegularComponents.rc_part_name,
    RegularComponents.rc_category,
    SUM(LocationsRegularComps.lrc_quantity) AS TotalQuantity,
    Locations.location_room_number,
    Locations.location_shelf_number,
    Sites.site_address_city
    FROM RegularComponents 
    INNER JOIN LocationsRegularComps ON RegularComponents.rc_pn=LocationsRegularComps.lrc_rc_pn
    INNER JOIN Locations ON Locations.location_id=LocationsRegularComps.lrc_location_id
    INNER JOIN Sites ON Locations.location_site_id=Sites.site_id
    WHERE RegularComponents.rc_part_name 
    LIKE '{}%' 
    ORDER BY RegularComponents.rc_part_name;
    """
    filter(filter_query_to_run=filter_query, data_to_filter=filtered_terms)



def filter_site(filter_site_id, filter_site_address_1, filter_site_address_2, filter_site_city, filter_site_state, filter_site_zip):

    # Load SQL query for filtering filter site data
    filter_site_query = """
    SELECT * 
    FROM Sites
    WHERE 
    site_id = %s OR
    site_address_1 = %s OR
    site_address_2 = %s OR
    site_address_city = %s OR
    site_address_state = %s OR
    site_address_postal_code
    ;
    """
    filter_site_data = (filter_site_id, filter_site_address_1, filter_site_address_2, filter_site_city, filter_site_state, filter_site_zip)
    filter(filter_query_to_run=filter_site_query, data_to_filter=filter_site_data)


def filter_work_order(filter_wo_open_date,filter_wo_close_date, filter_wo_status, filter_wo_reference_number, filter_wo_employee_id):

    # Load SQL query for filtering filter work order data
    filter_work_order_query = """
    SELECT * 
    FROM WorkOrders
    WHERE
    wo_open_date = %s OR
    wo_close_date = %s OR
    wo_status = %s OR
    wo_reference_number = %s OR
    wo_employee_id = %s
    ;
    """
    filter_workorder_data=(filter_wo_open_date, filter_wo_close_date, filter_wo_status, filter_wo_reference_number, filter_wo_employee_id)
    print(f'filter work order data is: {filter_workorder_data}')
    filter(filter_query_to_run=filter_work_order_query,data_to_filter=filter_workorder_data)


def filter_work_order_products(filter_wop_wo_id,filter_wop_product_sn):
    # Load SQL query for filtering work order/products data

    filter_work_order_products="""
    SELECT * 
    FROM WorkOrderProducts
    WHERE
    wop_wo_id = %s OR
    wop_product_sn = %s
    ;
    """
    filter_work_order_products_data=(filter_wop_wo_id,filter_wop_product_sn)
    filter(filter_query_to_run=filter_work_order_products,data_to_filter=filter_work_order_products_data)

    


def filter_employees(filter_employee_id, filter_employee_first_name, filter_employee_last_name,  
        filter_employee_email, filter_employee_group, filter_employee_site_id):

    # Load SQL query for filtering filter employee data
    filter_employee_query = """
    SELECT * 
    FROM Employees
    WHERE
    employee_id = %s OR
    employee_first_name = %s OR
    employee_last_name = %s OR
    employee_email = %s OR
    employee_group = %s OR
    employee_site_id = %s
    ;
    """
    filter_employee_data = (filter_employee_id, filter_employee_first_name, filter_employee_last_name,  
        filter_employee_email, filter_employee_group, filter_employee_site_id)
    filter(filter_query_to_run=filter_employee_query, data_to_filter=filter_employee_data)


def filter_locations(filter_location_room_number, filter_location_shelf_number, filter_location_site_id):

    # Load SQL query for filtering filter location data
    filter_location_query = """
    SELECT * 
    FROM Locations
    WHERE
    location_site_id = %s OR
    location_room_number = %s OR
    location_shelf_number
    ;
    """
    filter_location_data = (filter_location_room_number, filter_location_shelf_number, filter_location_site_id)
    print('filter_location_data', filter_location_data)
    filter(filter_query_to_run=filter_location_query, data_to_filter=filter_location_data)


# def filter_location_regular_comps():

#   # Load SQL query for filtering filter locations/regular components data
#   filter_location_regular_comps_query = """"""
#   filter(filter_query_to_run=filter_location_regular_comps_query)


# def filter_products_regular_comps():

#   # Load SQL query for filtering filter products/regular components data
#   filter_product_regular_comps_query = """"""
#   filter(filter_query_to_run=filter_product_regular_comps_query)


# def filter_products_special_comps():

#   # Load SQL query for filtering filter products/special components data
#   filter_product_special_comps_query = """"""
#   filter(filter_query_to_run=filter_product_special_comps_query)


def filter_product(filter_product_pn, filter_product_family, filter_product_date_assmebly, filter_product_qc_date,
    filter_product_warranty_expiration_date, filter_product_employee_id, filter_product_location_id, filter_product_sc_sn):

    # Load SQL query for filtering filter product data
    filter_product_query = """
    SELECT * 
    FROM Products
    WHERE
    filter_product_pn = %s OR
    filter_product_family = %s OR
    filter_product_date_assmebly = %s OR
    filter_product_qc_date = %s OR
    filter_product_warranty_expiration_date = %s OR
    filter_product_employee_id = %s OR
    filter_product_location_id = %s OR
    filter_product_sc_sn = %s
    ;
    """
    filter_product_data = (filter_product_pn, filter_product_family, filter_product_date_assmebly, filter_product_qc_date,
        filter_product_warranty_expiration_date, filter_product_employee_id, filter_product_location_id, filter_product_sc_sn)
    filter(filter_query_to_run=filter_product_query,data_to_filter=filter_product_data)
    
    

def filter_regular_components(filter_rc_category, filter_rc_part_name, filter_site_id, filter_room_number, filter_shelf_number):

    # Load SQL query for filtering filter regular component data
    filter_regular_component_query = """
    SELECT * 
    FROM RegularComponents
    INNER JOIN LocationsRegularComps ON RegularComponents.rc_pn = LocationsRegularComps.lrc_rc_pn
    INNER JOIN Locations ON Locations.location_id = LocationsRegularComps.lrc_location_id
    WHERE
    RegularComponents.rc_category = %s OR
    RegularComponents.rc_part_name = %s OR
    Locations.location_room_number = %s OR
    Locations.location_shelf_number = %s OR
    Locations.location_site_id
    ;
    """
    filter_regular_component_data = (filter_rc_category, filter_rc_part_name, filter_site_id, filter_room_number, filter_shelf_number)
    filter(filter_query_to_run=filter_regular_component_query, data_to_filter=filter_regular_component_data)

def filter_special_components(filter_sc_sn, filter_sc_pn, filter_site_id, filter_room_number, filter_shelf_number, filter_sc_is_free):

    # Load SQL query for filtering filter regular component data
    filter_special_component_query = """
    SELECT * 
    FROM SpecialComponents
    INNER JOIN Locations ON Locations.location_id = SpecialComponents.sc_location_id
    WHERE
    SpecialComponents.sc_sn = %s OR
    SpecialComponents.sc_pn = %s OR
    Locations.location_site_id
    Locations.location_room_number = %s OR
    Locations.location_shelf_number = %s OR
    SpecialComponents.sc_is_free = %s
    ;
    """
    filter_special_component_data = (filter_sc_sn, filter_sc_pn, filter_site_id, filter_room_number, filter_shelf_number, filter_sc_is_free)
    filter(filter_query_to_run=filter_special_component_query, data_to_filter=filter_special_component_data)

