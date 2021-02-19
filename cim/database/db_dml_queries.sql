-- Query for add a new site functionality with colon : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO Sites (site_address_1, site_address_2, site_address_city, site_address_state, site_address_postal_code)
VALUES (:site_address_1_input, :site_address_2_input, :site_address_city_input, :site_address_state_input, :site_address_postal_code_input);



-- Query for add a new work order functionality with : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO WorkOrders (wo_open_date, wo_close_date, wo_status, wo_reference_number, wo_employee_id)
VALUES (:wo_open_date_input, :wo_close_date_input, :wo_status_input, :wo_reference_number_input, :wo_employee_id_dropdown_input);



-- Query for add a new connection between work orders and products with : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO WorkOrderProducts (wop_wo_id, wop_product_sn)
VALUES (:work_order_id_from_dropdown_Input, :product_id_from_dropdown_Input);



-- Query for add a new employee functionality with : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO Employees (employee_group, employee_first_name, employee_last_name, employee_email, employee_password, employee_site_id)
VALUES (:employee_group_input, :employee_first_name_input, 
	:employee_last_name_input, :employee_email_input, :employee_password_input, :employee_site_id_dropdown_input);



-- Query for add a new character functionality with : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO Locations (fname, lname, homeworld, age)
VALUES (:fnameInput, :lnameInput, :homeworld_id_from_dropdown_Input, :ageInput);



-- Query for add a new connection between locations and regular components with : being used to 
-- denote the variables that will have data from the backend programming language

INSERT INTO LocationsRegularComps (lrc_quantity, lrc_location_id, lrc_rc_pn)
VALUES (:new_regular_component_quantity, :location_id_from_dropdown_Input, :regular_component_id_from_dropdown_Input);
