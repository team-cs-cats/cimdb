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


-- Populate Sites table with data
LOCK TABLES `Sites` WRITE;
/*!40000 ALTER TABLE `Sites` DISABLE KEYS */;
INSERT INTO `Sites` VALUES 
(12, '12745 Lampwood Road', 'Suite 612', 'Los Angeles', 'CA', '90023'),
(14, '26262 Shoreline Drive', NULL, 'San Francisco', 'CA', '94125'),
(16, '1984 Washoe Street', NULL, 'Reno', 'CA', '89523');
/*!40000 ALTER TABLE `Sites` ENABLE KEYS */;
UNLOCK TABLES;


-- Locations table Creation query
DROP TABLE IF EXISTS `Locations`;
CREATE TABLE `Locations` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `location_room_number` int NOT NULL,
  `location_shelf_number` int NOT NULL,
  `location_site_id` int NOT NULL,
  PRIMARY KEY (`location_id`)
  FOREIGN KEY (`location_site_id`) REFERENCES `Sites`(`site_id`) 
)ENGINE=INNODB;


-- Populate Locations table with data
LOCK TABLES `Locations` WRITE;
/*!40000 ALTER TABLE `Sites` DISABLE KEYS */;
INSERT INTO `Locations` VALUES 
(82584, 10, 20, 14), (84208, 16, 9, 16),(19515, 8, 3, 12), (58103, 10, 19, 12),(72147, 11, 5, 16), (72178, 3, 20, 16),
(52343, 19, 14, 12), (33248, 1, 12, 14),(39124, 7, 3, 14),(51656, 11, 1, 12),(21798, 3, 8, 16),
(46492, 5, 10, 16),(50921, 16, 7, 14),(17815, 19, 14, 14), (37588, 6, 11, 12), (32852, 5, 7, 12),(14369, 16, 18, 14), 
(23157, 18, 2, 12), (44176, 9, 7, 16), (99084, 9, 9, 16),(37394, 20, 3, 16), (17954, 11, 8, 16),(40009, 5, 5, 12),
(64808, 17, 10, 16), (43726, 16, 5, 16),(40717, 13, 5, 14), (19383, 10, 1, 12), (45806, 20, 6, 12),
(80056, 2, 8, 12),(79633, 10, 18, 14), (40258,1,19,12),(16656, 12, 13, 16), (46156, 6, 4, 14), (59739, 10, 5, 12), 
(56478, 11, 6, 16), (98569, 12, 19, 12),(95781, 14, 19, 14), (92746, 5, 10, 16), (75228, 6, 4, 16), (36790, 2, 2, 12), 
(18036, 1, 17, 12),(34207, 2, 8, 16), (57666, 10, 2, 14),(82694, 20, 8, 16), (27442, 9, 13, 16),
(41309, 11, 15, 14),(27956, 8, 2, 12), (26311, 15, 6, 12), (69472, 5, 19, 12), (16168, 12, 5, 16), (99862, 19, 15, 16), 
(82571, 14, 12, 16), (11190, 8, 20, 16),(72595, 5, 8, 14), (75255, 5, 9, 12), (81951, 13, 4, 12),(59740, 17, 4, 14),
(25712, 18, 2, 16), (15037, 5, 5, 14), (17407, 11, 17, 12), (72530, 4, 13, 14), (38684, 9, 18, 16),(49892, 6, 17, 14), 
(33837, 8, 18, 16), (13915, 18, 20, 12),(73322, 2, 4, 14), (49834, 18, 17, 12), (27929, 12, 8, 14),
(83281, 6, 1, 16), (58582, 19, 13, 12), (79122, 2, 11, 16), (77314, 3, 15, 16),(61913, 11, 14, 12), (54962, 14, 19, 12), 
(35589, 19, 17, 14), (25373, 15, 10, 12), (45162, 3, 9, 16), (29310, 12, 13, 16),(54924, 20, 11, 14), (10683, 2, 10, 16), 
(25525, 11, 3, 12), (71275, 12, 6, 16), (74877, 5, 10, 16), (11301, 16, 16, 12),(62446, 16, 13, 16), (54058, 1, 19, 16), 
(14777, 15, 1, 16), (58048, 8, 9, 14), (11340, 2, 17, 16), (17445, 10, 3, 16), (35047, 19, 13, 14), (63001, 16, 1, 14), 
(49051, 20, 5, 16), (47933, 1, 16, 14), (90843, 16, 18, 16),(13505, 19, 9, 16), (71619, 12, 18, 14),
(72624, 15, 4, 14), (55634, 17, 5, 14), (47385, 5, 14, 12),(47933, 0, 0, 12), (90843, 0, 0, 14), (13505, 0, 0, 16),
(71619, 0, 1, 12),(72624, 0, 1, 14), (55634, 0, 1, 16); 
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
