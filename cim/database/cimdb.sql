-- filename: cimdb.sql
-- Description: provides a location for the table structure of the base entities for the CIMDB

-- initialization of database
CREATE DATABASE IF NOT EXISTS cimdb;
USE cimdb;
SHOW tables;


-- Site table Creation query
DROP TABLE IF EXISTS `Sites`;
CREATE TABLE `Sites` (
  `site_id` int NOT NULL AUTO_INCREMENT,
  `site_address_1` varchar(255) NOT NULL,
  `site_address_2` varchar(255),
  `site_address_city` varchar(255) NOT NULL,
  `site_address_state` varchar(255) NOT NULL,
  `site_address_postal_code` varchar(255) NOT NULL,
  PRIMARY KEY (`site_id`)
) ENGINE=INNODB;


-- Add site data to database

LOCK TABLES `Sites` WRITE;
/*!40000 ALTER TABLE `Sites` DISABLE KEYS */;
INSERT INTO `Sites` VALUES 
(12, '12745 Lampwood Road', 'Suite 612', 'Los Angeles', 'CA', '90023'),
(14, '26262 Shoreline Drive', NULL, 'San Francisco', 'CA', '94125'),
(16, '1984 Washoe Street', NULL, 'Reno', 'CA', '89523');
/*!40000 ALTER TABLE `Sites` ENABLE KEYS */;
UNLOCK TABLES;


-- DROP TABLE IF EXISTS `Products`;
-- CREATE TABLE `Products` (
--   `product_sn` int,
--   `product_pn` char(16),
--   `product_family` varchar(255),
--   `product_date_assembly` date,
--   `product_qc_date` date,
--   `product_warranty_expiration_date` date,
--   `product_employee_id` int,
--   `product_location_id` int,
--   `product_sc_sn` int,
--   PRIMARY KEY (`product_sn`)
-- );

-- DROP TABLE IF EXISTS `WorkOrderProducts`;
-- CREATE TABLE `WorkOrderProducts` (
--   `wop_id` int NOT NULL AUTO_INCREMENT,
--   `wop_wo_id` int,
--   `wop_product_sn` int,
--   PRIMARY KEY (`wop_id`)
-- );

-- DROP TABLE IF EXISTS `Locations`;
-- CREATE TABLE `Locations` (
--   `location_id` int NOT NULL AUTO_INCREMENT,
--   `location_room_number` int,
--   `location_shelf_number` int,
--   `location_site_id` int,
--   PRIMARY KEY (`location_id`)
-- );

-- DROP TABLE IF EXISTS `ProductsRegularComps`;
-- CREATE TABLE `ProductsRegularComps` (
--   `prc_id` int NOT NULL AUTO_INCREMENT,
--   `prc_product_sn` int,
--   `prc_rc_pn` int,
--   `prc_quantity_needed` int,
--   PRIMARY KEY (`prc_id`)
-- );

-- DROP TABLE IF EXISTS `Employees`;
-- CREATE TABLE `Employees` (
--   `employee_id` int NOT NULL AUTO_INCREMENT,
--   `employee_group` varchar(255),
--   `employee_first_name` varchar(255),
--   `employee_last_name` varchar(255),
--   `employee_email` varchar(255),
--   `employee_password` varchar(255),
--   `employee_site_id` int,
--   PRIMARY KEY (`employee_id`)
-- );

-- DROP TABLE IF EXISTS `WorkOrders`;
-- CREATE TABLE `WorkOrders` (
--   `wo_id` int NOT NULL AUTO_INCREMENT,
--   `wo_open_date` date,
--   `wo_close_date` date,
--   `wo_status` varchar(255),
--   `wo_reference_number` int,
--   `wo_employee_id` int,
--   PRIMARY KEY (`wo_id`)
-- );

-- DROP TABLE IF EXISTS `SpecialComponents`;
-- CREATE TABLE `SpecialComponents` (
--   `sc_sn` int NOT NULL AUTO_INCREMENT,
--   `sc_pn` char(16),
--   `sc_is_free` boolean,
--   `sc_product_sn` int,
--   `sc_location_id` int,
--   PRIMARY KEY (`sc_sn`)
-- );

-- DROP TABLE IF EXISTS `RegularComponents`;
-- CREATE TABLE `RegularComponents` (
--   `rc_pn` int NOT NULL AUTO_INCREMENT,
--   `rc_category` varchar(255),
--   PRIMARY KEY (`rc_pn`)
-- );

-- DROP TABLE IF EXISTS `LocationsRegularComps`;
-- CREATE TABLE `LocationsRegularComps` (
--   `lrc_id` int NOT NULL AUTO_INCREMENT,
--   `lrc_location_id` int,
--   `lrc_rc_pn` int,
--   `lrc_quantity` int,
--   PRIMARY KEY (`lrc_id`)
-- );
