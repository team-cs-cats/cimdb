-- DML Selection query for sites
SELECT * FROM Sites WHERE site_id = :site_id_input

-- Query for add a new site functionality with colon : being used to 
-- denote the variables that will have data from the backend programming language
INSERT INTO Sites (site_address_1, site_address_2, site_address_city, site_address_state, site_address_postal_code)
VALUES (:site_address_1_input, :site_address_2_input, :site_address_city_input, :site_address_state_input, :site_address_postal_code_input);

-- Deletion query for site
DELETE FROM Sites WHERE site_id=:site_id_from_delete_button;

-- Updation query for site
UPDATE Sites SET 
site_address_1 = :edit_site_address_1, 
site_address_2 = :edit_site_address_2, 
site_address_city = :edit_site_address_city, 
site_address_state = :edit_site_address_state, 
site_address_postal_code = :edit_site_address_postal_code
WHERE site_id = :site_id_from_update_button




-- DML Selection query for work orders
SELECT * FROM WorkOrders WHERE wo_id = :wo_id_input

-- Query for add a new work order functionality with : being used to 
-- denote the variables that will have data from the backend programming language
INSERT INTO WorkOrders (wo_open_date, wo_close_date, wo_status, wo_reference_number, wo_employee_id)
VALUES (:wo_open_date_input, :wo_close_date_input, :wo_status_input, :wo_reference_number_input, :wo_employee_id_dropdown_input);

-- Deletion query for work order
DELETE FROM WorkOrders WHERE wo_id=:wo_id_from_delete_button;

-- Updation query for work order
UPDATE WorkOrders SET wo_open_date = :edit_wo_open_date_input, 
wo_close_date = :edit_wo_close_date_input, 
wo_status = :edit_wo_status_input, 
wo_reference_number = :edit_wo_reference_number_input, 
wo_employee_id = :edit_wo_employee_id_dropdown_input, 
WHERE wo_id = :wo_id_from_update_button





-- DML Selection query for WorkOrderProducts
SELECT * FROM WorkOrderProducts WHERE wop_id = :wop_id_input

-- Query for add a new connection between work orders and products with : being used to 
-- denote the variables that will have data from the backend programming language
INSERT INTO WorkOrderProducts (wop_wo_id, wop_product_sn)
VALUES (:work_order_id_from_dropdown_Input, :product_id_from_dropdown_Input);

-- Deletion query for WorkOrderProducts
DELETE FROM WorkOrderProducts WHERE wop_id=:wop_id_from_delete_button;

-- Updation query for WorkOrderProducts
UPDATE WorkOrderProducts SET 
wop_wo_id = :edit_wop_wo_id, 
wop_product_sn = :edit_wop_product_sn
WHERE wop_id = :wop_id_from_update_button





-- DML Selection query for Employees
SELECT * FROM Employees WHERE site_id = :site_id_input

-- Query for add a new employee functionality with : being used to 
-- denote the variables that will have data from the backend programming language
INSERT INTO Employees (employee_group, employee_first_name, employee_last_name, employee_email, employee_password, employee_site_id)
VALUES (:employee_group_input, :employee_first_name_input, 
	:employee_last_name_input, :employee_email_input, :employee_password_input, :employee_site_id_dropdown_input);

-- Deletion query for Employee
DELETE FROM Employees WHERE employee_id=:employee_id_from_delete_button;

-- Updation query for Employee
UPDATE Employees SET 
 employee_group = :employee_group_input,
 employee_first_name = :employee_first_name_input,
 employee_last_name = :employee_last_name_input,
 employee_email = :employee_email_input,
 employee_password = :employee_password_input,
 employee_site_id = :employee_site_id_dropdown_input
WHERE employee_id = :employee_id_from_update_button





-- DML Selection query for locations
SELECT * FROM Locations WHERE location_id = :location_id_input

-- Query for add a new location functionality with : being used to 
-- denote the variables that will have data from the backend programming language
INSERT INTO Locations (location_room_number, location_shelf_number, location_site_id)
VALUES (:location_room_number_input, :location_shelf_number_input, :location_site_id_dropdown_input);

-- Deletion query for locations
DELETE FROM Locations WHERE location_id=:location_id_from_delete_button;

-- Updation query for locations
UPDATE Locations SET 
 location_room_number = :location_room_number_input,
 location_shelf_number = :location_shelf_number_input,
 location_site_id = :location_site_id_dropdown_input
WHERE location_id = :location_id_from_update_button




-- DML Selection query for LocationsRegularComps
SELECT * FROM LocationsRegularComps WHERE lrc_id = :lrc_id_input

-- Query for add a new connection between locations and regular components with : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO LocationsRegularComps (lrc_quantity, lrc_location_id, lrc_rc_pn)
VALUES (:new_regular_component_quantity, :location_id_from_dropdown_Input, :regular_component_id_from_dropdown_Input);


-- Deletion query for LocationsRegularComps
DELETE FROM LocationsRegularComps WHERE lrc_id=:lrc_id_from_delete_button;

-- Updation query for LocationsRegularComps
UPDATE LocationsRegularComps SET 
lrc_quantity = :new_regular_component_quantity, 
lrc_location_id = :location_id_from_dropdown_Input, 
lrc_rc_pn = :regular_component_id_from_dropdown_Input
WHERE lrc_id = :lrc_id_from_update_button






