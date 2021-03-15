-- filename: cimdb.sql
-- Description: provides a location for the table structure of the base entities for the CIMDB

-- initialization of database
UNLOCK tables;

-- Commented this out to run correctly on PHPMyAdmin
-- CREATE DATABASE IF NOT EXISTS cs340_hollaasa_cimdb;
-- USE cimdb;
SHOW tables;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS `ProductsRegularComps`;
DROP TABLE IF EXISTS `WorkOrderProducts`;
DROP TABLE IF EXISTS `Products`;
DROP TABLE IF EXISTS `LocationsRegularComps`;
DROP TABLE IF EXISTS `SpecialComponents`;
DROP TABLE IF EXISTS `RegularComponents`;
DROP TABLE IF EXISTS `WorkOrders`;
DROP TABLE IF EXISTS `Employees`;
DROP TABLE IF EXISTS `Locations`;
DROP TABLE IF EXISTS `Sites`;


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
  FOREIGN KEY (`location_site_id`) REFERENCES `Sites`(`site_id`) ON UPDATE CASCADE
)ENGINE=INNODB;


-- Populate Locations table with data
-- Keeping 1, 0, 0, 1 as Customer Location, and keeping locations for Reno
LOCK TABLES `Locations` WRITE;
INSERT INTO `Locations` 
VALUES 
(1, 0, 0, 1), 
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
  FOREIGN KEY (`employee_site_id`) REFERENCES `Sites`(`site_id`) ON UPDATE CASCADE
);

-- Populate Employees table with data
LOCK TABLES `Employees` WRITE;
INSERT INTO `Employees` VALUES 
(14324,"supervisor","Pam","Luddy","pluddy6@2fast4you.com","CcBwnjq", 16),
(61764,"production","Kaiser","Reina","kreina4@2fast4you.com","KnrAKdA", 16),
(35477,"production","Giulia","Comberbeach","gcomberbeach7@2fast4you.com","oxAFg4t", 16),
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
  FOREIGN KEY (`wo_employee_id`) REFERENCES `Employees`(`employee_id`) ON UPDATE CASCADE
);


-- Populate WorkOrders table with data
-- Work Order 879845 is assigned to Employee 61764 "Kaiser","Reina" from Site ID 16 (Reno)
-- Work Order 815348 is assigned to Employee 39816 "Kalindi","Shulem" from Site ID 16 (Reno),
-- Work Order 845236 is assigned to Employee 35477 "Giulia","Comberbeach" from Site ID 16 (Reno);
LOCK TABLES `WorkOrders` WRITE;
INSERT INTO `WorkOrders` VALUES 
(879845, "2021-01-29", null, "assembly_pending", 84596, 61764),
(815348, "2021-01-12", null, "qc_pending", 84325, 39816),
(845236, "2021-01-24", "2021-01-16", "shipping_pending", 23165, 35477);
UNLOCK TABLES;


-- RegularComponents table Creation query
DROP TABLE IF EXISTS `RegularComponents`;
CREATE TABLE `RegularComponents` (
  `rc_pn` int NOT NULL AUTO_INCREMENT,
  `rc_pn_desc` varchar(16) NOT NULL, 
  `rc_category` varchar(255) NOT NULL,
  PRIMARY KEY (`rc_pn`)
);


-- Populate RegularComponents table with data
LOCK TABLES `RegularComponents` WRITE;
INSERT INTO `RegularComponents` VALUES 
(1,"MB 1", "MB"),
(2,"MB 2", "MB"),
(3,"MB 3", "MB"),
(50,"RAM 1", "RAM"),
(51,"RAM 2", "RAM"),
(52,"RAM 3", "RAM"),
(100,"Case 1", "Case"),
(101,"Case 2", "Case"),
(102,"Case 3", "Case"),
(150,"HDD 1", "HDD"),
(151,"HDD 2", "HDD"),
(152,"HDD 3", "HDD"),
(200,"NO GC", "GC"),
(201,"GC 1", "GC"),
(202,"GC 2", "GC");
UNLOCK TABLES;



-- LocationsRegularComps table Creation query
DROP TABLE IF EXISTS `LocationsRegularComps`;
CREATE TABLE `LocationsRegularComps` (
  `lrc_id` int NOT NULL AUTO_INCREMENT,
  `lrc_location_id` int ,
  `lrc_rc_pn` int,
  `lrc_quantity` int NOT NULL,
  PRIMARY KEY (`lrc_id`),
  FOREIGN KEY (`lrc_location_id`) REFERENCES `Locations`(`location_id`) ON UPDATE CASCADE,
  FOREIGN KEY (`lrc_rc_pn`) REFERENCES `RegularComponents`(`rc_pn`) ON UPDATE CASCADE
);



-- Populate LocationsRegularComps table with data
LOCK TABLES `LocationsRegularComps` WRITE;
INSERT INTO `LocationsRegularComps` 
(lrc_id,  lrc_location_id,  lrc_rc_pn,  lrc_quantity) VALUES 
(1, 4,                        1,        0),  
(2, 64,                     2,        1),  
(3, 69,                     3,        3),  
(4, 43,                     50,       14),  
(5, 14,                      51,       25),  
(6, 35,                     52,       0),  
(7, 45,                     150,        234),  
(8, 15,                     151,        62),  
(9, 30,                     152,        73),  
(10, 68,                     1,        25),  
(11, 34,                     2,        74),  
(12, 31,                     3,        95),  
(13, 13,                     50,       4),  
(14, 24,                     51,       0),  
(15, 72,                     52,       0),  
(16, 57,                     150,        234),  
(17, 29,                     151,        7),  
(18, 58,                     152,        33),  
(19, 67,                     1,        0),  
(20, 5,                      2,        237),  
(21, 61,                     3,        88),  
(22, 65,                     50,       81),  
(23, 59,                     51,       26),  
(24, 54,                      52,       0),  
(25, 11,                     150,        42),  
(26, 25,                     151,        27),  
(27, 71,                    152,        25),  
(28, 38,                    1,        238),  
(29, 7,                      2,        42),  
(30, 53,                   3,        265),  
(31, 40,                   50,       23),  
(32, 26,                      51,       8),  
(33, 63,                   52,       0),  
(34, 48,                   150,        0),  
(35, 16,                   151,        2),  
(36, 22,                   152,        4)  
;
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
  -- FOREIGN KEY (`sc_product_sn`) REFERENCES `Products`(`product_sn`), 
  -- commented out because the Special Component does not care about the product it is in.
  -- We need to add Special Components to the database first, then link them to Products.
  FOREIGN KEY (`sc_location_id`) REFERENCES `Locations`(`location_id`) ON UPDATE CASCADE
);


-- Populate SpecialComponents table with data
LOCK TABLES `SpecialComponents` WRITE;
INSERT INTO `SpecialComponents` 
(`sc_sn`, `sc_pn`, `sc_is_free`, `sc_product_sn`, `sc_location_id`)
VALUES 
(3000, "i3", 0, null, 57),
(3001, "i3", 0, null, 57),
(3002, "i3", 0, null, 57),
(3003, "i3", 1, null, 57),
(3004, "i3", 1, null, 57),
(3005, "i3", 1, null, 57),
(3006, "i3", 1, null, 57),
(3007, "i3", 1, null, 57),
(3008, "i3", 1, null, 57),
(3009, "i3", 1, null, 57),
(5000, "i5", 1, null, 57),
(5001, "i5", 0, null, 57),
(5002, "i5", 0, null, 57),
(5003, "i5", 0, null, 57),
(5004, "i5", 1, null, 57),
(5005, "i5", 1, null, 57),
(5006, "i5", 1, null, 57),
(5007, "i5", 1, null, 57),
(5008, "i5", 1, null, 57),
(5009, "i5", 1, null, 57),
(7000, "i7", 0, null, 57),
(7001, "i7", 0, null, 57),
(7002, "i7", 0, null, 57),
(7003, "i7", 1, null, 57),
(7004, "i7", 1, null, 57),
(7005, "i7", 1, null, 57),
(7006, "i7", 1, null, 57),
(7007, "i7", 1, null, 57),
(7008, "i7", 1, null, 57),
(7009, "i7", 1, null, 57);
UNLOCK TABLES;



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
  FOREIGN KEY (`product_employee_id`) REFERENCES `Employees`(`employee_id`) ON UPDATE CASCADE,
  FOREIGN KEY (`product_location_id`) REFERENCES `Locations`(`location_id`) ON UPDATE CASCADE,

  -- Here, this links to existing Special Components, which have to be in the database first.
  FOREIGN KEY (`product_sc_sn`) REFERENCES `SpecialComponents`(`sc_sn`) ON UPDATE CASCADE
);

-- Populate Products table with data
LOCK TABLES `Products` WRITE;
INSERT INTO `Products` 
(`product_sn`, `product_pn`, `product_family`, `product_date_assembly`, `product_qc_date`, 
  `product_warranty_expiration_date`, `product_employee_id`, `product_location_id`, `product_sc_sn`)
VALUES 
(1,"Pro-i3", "Pro","2020-12-20","2020-12-12","2021-12-21",61764,57,3001),
(2,"Pro-i3", "Pro","2020-12-20","2020-12-12","2021-12-21",39816,57,3002),
(3,"Basic-i3", "Basic","2020-12-20","2020-12-12","2021-12-21",35477,57,3003),
(4,"Pro-i5", "Pro","2020-12-20","2020-12-12","2021-12-21",61764,57,5001),
(5,"Pro-i5", "Pro","2020-12-20","2020-12-12","2021-12-21",39816,57,5002),
(6,"Basic-i5", "Basic","2020-12-20","2020-12-12","2021-12-21",35477,57,5003),
(7,"Pro-i7", "Pro","2020-12-20","2020-12-12","2021-12-21",61764,57,7001),
(8,"Basic-i7", "Basic","2020-12-20","2020-12-12","2021-12-21",39816,57,7002),
(9,"Basic-i7", "Basic","2020-12-20","2020-12-12","2021-12-21",35477,57,7003),
(10,"Pro-i7", "Pro","2020-12-20","2020-12-12","2021-12-21",61764,57,7004);
UNLOCK TABLES;



-- WorkOrderProducts table Creation query
DROP TABLE IF EXISTS `WorkOrderProducts`;
CREATE TABLE `WorkOrderProducts` (
  `wop_id` int NOT NULL AUTO_INCREMENT,
  `wop_wo_id` int,
  `wop_product_sn` int,
  PRIMARY KEY (`wop_id`),
  FOREIGN KEY (`wop_wo_id`) REFERENCES `WorkOrders`(`wo_id`) ON UPDATE CASCADE,
  FOREIGN KEY (`wop_product_sn`) REFERENCES `Products`(`product_sn`) ON UPDATE CASCADE
);


-- Populate WorkOrderProducts table with data
LOCK TABLES `WorkOrderProducts` WRITE;
INSERT INTO `WorkOrderProducts` VALUES 
(1,879845,1),
(2,815348,2),
(3,845236,3),
(4,879845,4),
(5,815348,5),
(6,845236,6),
(7,879845,7),
(8,815348,8),
(9,845236,9),
(10,879845,10);
UNLOCK TABLES;


-- ProductsRegularComps table Creation query
DROP TABLE IF EXISTS `ProductsRegularComps`;
CREATE TABLE `ProductsRegularComps` (
  `prc_id` int NOT NULL AUTO_INCREMENT,
  `prc_product_sn` int,
  `prc_rc_pn` int,
  `prc_quantity_needed` int NOT NULL,
  PRIMARY KEY (`prc_id`),
  FOREIGN KEY (`prc_product_sn`) REFERENCES `Products`(`product_sn`) ON UPDATE CASCADE,
  FOREIGN KEY (`prc_rc_pn`) REFERENCES `RegularComponents`(`rc_pn`) ON UPDATE CASCADE
);

-- Populate ProductsRegularComps table with data
LOCK TABLES `ProductsRegularComps` WRITE;
INSERT INTO `ProductsRegularComps` VALUES 
(1,1,1,1),
(2,1,50,2),
(3,1,100,1),
(4,1,150,2),
(5,1,200,1),
(6,2,3,1),
(7,2,51,3),
(8,2,102,1),
(9,2,152,1),
(10,2,200,1),
(11,3,3,1),
(12,3,52,3),
(13,3,100,1),
(14,3,151,3),
(15,3,202,1),
(16,4,3,1),
(17,4,50,2),
(18,4,100,1),
(19,4,150,2),
(20,4,200,1);
UNLOCK TABLES;




SET FOREIGN_KEY_CHECKS = 1;
