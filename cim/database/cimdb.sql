-- filename: cimdb.sql
-- Description: provides a location for the table structure of the base entities for the CIMDB


DROP TABLE IF EXISTS `Products`;
CREATE TABLE `Products` (
  `product_sn` int,
  `product_pn` char(16),
  `product_family` varchar(255),
  `product_date_assembly` date,
  `product_qc_date` date,
  `product_warranty_expiration_date` date,
  `product_employee_id` int,
  `product_location_id` int,
  `product_sc_sn` int,
  PRIMARY KEY (`product_sn`)
);

DROP TABLE IF EXISTS `Products`;
CREATE TABLE `WorkOrderProducts` (
  `wop_id` int,
  `wop_wo_id` int,
  `wop_product_sn` int,
  PRIMARY KEY (`wop_id`)
);

CREATE TABLE `Sites` (
  `site_id` int,
  `site_address_1` varchar(255),
  `site_address_2` varchar(255),
  `site_address_city` varchar(255),
  `site_address_state` varchar(255),
  `site_address_postal_code` varchar(255),
  PRIMARY KEY (`site_id`)
);

CREATE TABLE `Locations` (
  `location_id` int,
  `location_room_number` int,
  `location_shelf_number` int,
  `location_site_id` int,
  PRIMARY KEY (`location_id`)
);

CREATE TABLE `ProductsRegularComps` (
  `prc_id` int,
  `prc_product_sn` int,
  `prc_rc_pn` int,
  `prc_quantity_needed` int,
  PRIMARY KEY (`prc_id`)
);

CREATE TABLE `Employees` (
  `employee_id` int,
  `employee_group` varchar(255),
  `employee_first_name` varchar(255),
  `employee_last_name` varchar(255),
  `employee_email` varchar(255),
  `employee_password` varchar(255),
  `employee_site_id` int,
  PRIMARY KEY (`employee_id`)
);

CREATE TABLE `WorkOrders` (
  `wo_id` int,
  `wo_open_date` date,
  `wo_close_date` date,
  `wo_status` varchar(255),
  `wo_reference_number` int,
  `wo_employee_id` int,
  PRIMARY KEY (`wo_id`)
);

CREATE TABLE `SpecialComponents` (
  `sc_sn` int,
  `sc_pn` char(16),
  `sc_is_free` boolean,
  `sc_product_sn` int,
  `sc_location_id` int,
  PRIMARY KEY (`sc_sn`)
);

CREATE TABLE `RegularComponents` (
  `rc_pn` int,
  `rc_category` varchar(255),
  PRIMARY KEY (`rc_pn`)
);

CREATE TABLE `LocationsRegularComps` (
  `lrc_id` int,
  `lrc_location_id` int,
  `lrc_rc_pn` int,
  `lrc_quantity` int,
  PRIMARY KEY (`lrc_id`)
);
