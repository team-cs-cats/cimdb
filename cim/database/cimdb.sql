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
INSERT INTO `Sites` VALUES 
(1, 'Customer', 'Customer', 'Customer', 'CA', '99999'),
(12, '12745 Lampwood Road', 'Suite 612', 'Los Angeles', 'CA', '90023'),
(14, '26262 Shoreline Drive', NULL, 'San Francisco', 'CA', '94125'),
(16, '1984 Washoe Street', NULL, 'Reno', 'CA', '89523');
UNLOCK TABLES;


-- Locations table Creation query
DROP TABLE IF EXISTS `Locations`;
CREATE TABLE `Locations` (
  `location_id` int NOT NULL AUTO_INCREMENT,
  `location_room_number` int NOT NULL,
  `location_shelf_number` int NOT NULL,
  `location_site_id` int NOT NULL,
  PRIMARY KEY (`location_id`),
  FOREIGN KEY (`location_site_id`) REFERENCES `Sites`(`site_id`) 
)ENGINE=INNODB;


-- Populate Locations table with data
LOCK TABLES `Locations` WRITE;
INSERT INTO `Locations` VALUES 
(1, 0, 0, 1),
(2, 1, 1, 12), (3, 1, 2, 12), (4, 1, 3, 12), (5, 1, 4, 12), (6, 1, 5, 12), 
(7, 2, 1, 12), (8, 2, 2, 12), (9, 2, 3, 12), (10, 2, 4, 12), (11, 2, 5, 12), 
(12, 3, 1, 12), (13, 3, 2, 12), (14, 3, 3, 12), (15, 3, 4, 12), (16, 3, 5, 12), 
(17, 4, 1, 12), (18, 4, 2, 12), (19, 4, 3, 12), (20, 4, 4, 12), (21, 4, 5, 12), 
(22, 5, 1, 12), (23, 5, 2, 12), (24, 5, 3, 12), (25, 5, 4, 12), (26, 5, 5, 12), 
(27, 1, 1, 14), (28, 1, 2, 14), (29, 1, 3, 14), (30, 1, 4, 14), (31, 1, 5, 14), 
(32, 2, 1, 14), (33, 2, 2, 14), (34, 2, 3, 14), (35, 2, 4, 14), (36, 2, 5, 14), 
(37, 3, 1, 14), (38, 3, 2, 14), (39, 3, 3, 14), (40, 3, 4, 14), (41, 3, 5, 14), 
(42, 4, 1, 14), (43, 4, 2, 14), (44, 4, 3, 14), (45, 4, 4, 14), (46, 4, 5, 14), 
(47, 5, 1, 14), (48, 5, 2, 14), (49, 5, 3, 14), (50, 5, 4, 14), (51, 5, 5, 14), 
(52, 1, 1, 16), (53, 1, 2, 16), (54, 1, 3, 16), (55, 1, 4, 16), (56, 1, 5, 16), 
(57, 2, 1, 16), (58, 2, 2, 16), (59, 2, 3, 16), (60, 2, 4, 16), (61, 2, 5, 16), 
(62, 3, 1, 16), (63, 3, 2, 16), (64, 3, 3, 16), (65, 3, 4, 16), (66, 3, 5, 16), 
(67, 4, 1, 16), (68, 4, 2, 16), (69, 4, 3, 16), (70, 4, 4, 16), (71, 4, 5, 16), 
(72, 5, 1, 16), (73, 5, 2, 16), (74, 5, 3, 16), (75, 5, 4, 16), (76, 5, 5, 16);
UNLOCK TABLES;


-- Employees table Creation query
DROP TABLE IF EXISTS `Employees`;
CREATE TABLE `Employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `employee_group` varchar(255),
  `employee_first_name` varchar(255),
  `employee_last_name` varchar(255),
  `employee_email` varchar(255),
  `employee_password` varchar(255),
  `employee_site_id` int,
  PRIMARY KEY (`employee_id`),
  FOREIGN KEY (`employee_site_id`) REFERENCES `Sites`(`site_id`)
);

-- Populate Employees table with data
LOCK TABLES `Employees` WRITE;
INSERT INTO `Employees` VALUES 
(74253,"supervisor","Karlan","Lepard","klepard1@2fast4you.com","L32nLN0", 12),
(77644,"supervisor","Hayes","Leades","hleades2@2fast4you.com","7nRJect", 14),
(14324,"supervisor","Pam","Luddy","pluddy6@2fast4you.com","CcBwnjq", 16),
(77919,"production","Ursulina","Aikin","uaikin0@2fast4you.com","UMTJP38H", 12),
(60126,"production","Hervey","Wykes","hwykes3@2fast4you.com","yEKKJA", 14),
(61764,"production","Kaiser","Reina","kreina4@2fast4you.com","KnrAKdA", 16),
(58873,"production","Trudie","Calvie","tcalvie2@2fast4you.com","DUw9pMv6mgc", 12),
(46535,"production","Melodee","Duff","mduff5@2fast4you.com","xj91eB93aHEf", 14),
(35477,"production","Giulia","Comberbeach","gcomberbeach7@2fast4you.com","oxAFg4t", 16),
(17597,"production","Antonie","Gepp","agepp6@2fast4you.com","4MHKqvgRahlu", 12),
(97633,"production","Shawn","Boxell","sboxell7@2fast4you.com","GEFXwPR", 14),
(39816,"production","Kalindi","Shulem","kshulem0@2fast4you.com","DJi02w0oV2", 16);
UNLOCK TABLES;



-- WorkOrders table Creation query
DROP TABLE IF EXISTS `WorkOrders`;
CREATE TABLE `WorkOrders` (
  `wo_id` int NOT NULL AUTO_INCREMENT,
  `wo_open_date` date NOT NULL,
  `wo_close_date` date,
  `wo_status` varchar(255) NOT NULL,
  `wo_reference_number` int NOT NULL,
  `wo_employee_id` int,
  PRIMARY KEY (`wo_id`),
  FOREIGN KEY (`wo_employee_id`) REFERENCES `Employees`(`employee_id`)
);


-- Populate WorkOrders table with data
LOCK TABLES `WorkOrders` WRITE;
INSERT INTO `WorkOrders` VALUES 
(879845, "2021-01-29", null, "assembly_pending", 84596, 77919),
(815348, "2021-01-12", null, "qc_pending", 84325, 60126),
(968412, "2021-01-02", null, "assembly_pending", 98125, 58873),
(874523, "2021-01-22", null, "qc_pending", 98214, 46535),
(845236, "2021-01-24", "2021-01-16", "completed", 23165, 17597),
(658412, "2021-01-12", null, "qc_pending", 87462, 97633),
(874596, "2021-01-14", null, "shipping_pending", 841256, 58873),
(512648, "2021-01-21", null, "shipping_pending", 68451, 35477);
UNLOCK TABLES;



-- SpecialComponents table Creation query
DROP TABLE IF EXISTS `SpecialComponents`;
CREATE TABLE `SpecialComponents` (
  `sc_sn` int NOT NULL AUTO_INCREMENT,
  `sc_pn` char(16) NOT NULL,
  `sc_is_free` boolean NOT NULL,
  `sc_product_sn` int,
  `sc_location_id` int,
  PRIMARY KEY (`sc_sn`),
  FOREIGN KEY (`sc_product_sn`) REFERENCES `Products`(`product_sn`),
  FOREIGN KEY (`sc_location_id`) REFERENCES `Locations`(`location_id`)
);


-- RegularComponents table Creation query
DROP TABLE IF EXISTS `RegularComponents`;
CREATE TABLE `RegularComponents` (
  `rc_pn` int NOT NULL AUTO_INCREMENT,
  `rc_category` varchar(255) NOT NULL,
  PRIMARY KEY (`rc_pn`)
);

-- Products table Creation query
DROP TABLE IF EXISTS `Products`;
CREATE TABLE `Products` (
  `product_sn` int NOT NULL AUTO_INCREMENT,
  `product_pn` char(16) NOT NULL,
  `product_family` varchar(255) NOT NULL,
  `product_date_assembly` date,
  `product_qc_date` date,
  `product_warranty_expiration_date` date,
  `product_employee_id` int,
  `product_location_id` int,
  `product_sc_sn` int,
  PRIMARY KEY (`product_sn`),
  FOREIGN KEY (`product_employee_id`) REFERENCES `Employees`(`employee_id`),
  FOREIGN KEY (`product_location_id`) REFERENCES `Locations`(`location_id`),
  FOREIGN KEY (`product_sc_sn`) REFERENCES `SpecialComponents`(`sc_sn`)
);

-- WorkOrderProducts table Creation query
DROP TABLE IF EXISTS `WorkOrderProducts`;
CREATE TABLE `WorkOrderProducts` (
  `wop_id` int NOT NULL AUTO_INCREMENT,
  `wop_wo_id` int,
  `wop_product_sn` int,
  PRIMARY KEY (`wop_id`),
  FOREIGN KEY (`wop_wo_id`) REFERENCES `WorkOrders`(`wo_id`),
  FOREIGN KEY (`wop_product_sn`) REFERENCES `Products`(`product_sn`)
);

-- ProductsRegularComps table Creation query
DROP TABLE IF EXISTS `ProductsRegularComps`;
CREATE TABLE `ProductsRegularComps` (
  `prc_id` int NOT NULL AUTO_INCREMENT,
  `prc_product_sn` int,
  `prc_rc_pn` int,
  `prc_quantity_needed` int NOT NULL,
  PRIMARY KEY (`prc_id`),
  FOREIGN KEY (`prc_product_sn`) REFERENCES `Product`(`product_sn`),
  FOREIGN KEY (`prc_rc_pn`) REFERENCES `RegularComponents`(`rc_pn`)
);


-- LocationsRegularComps table Creation query
DROP TABLE IF EXISTS `LocationsRegularComps`;
CREATE TABLE `LocationsRegularComps` (
  `lrc_id` int NOT NULL AUTO_INCREMENT,
  `lrc_location_id` int ,
  `lrc_rc_pn` int,
  `lrc_quantity` int NOT NULL,
  PRIMARY KEY (`lrc_id`),
  FOREIGN KEY (`lrc_location_id`) REFERENCES `Locations`(`location_id`),
  FOREIGN KEY (`lrc_rc_pn`) REFERENCES `RegularComponents`(`rc_pn`)
);

SET FOREIGN_KEY_CHECKS = 1;