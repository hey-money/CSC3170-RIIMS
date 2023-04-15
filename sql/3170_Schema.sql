SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `Pro` ;
CREATE SCHEMA IF NOT EXISTS `Pro` DEFAULT CHARACTER SET utf8 ;
USE `Pro` ;

-- -----------------------------------------------------
-- Create below: Table `Pro`.`order_details`
-- -----------------------------------------------------
CREATE TABLE `order_details` (
	`ORDER_ID` VARCHAR(10) NOT NULL,
    `FOOD_ID` VARCHAR(10) NOT NULL,
    `QUANTITY` DECIMAL(3,0) NOT NULL,
    PRIMARY KEY (`ORDER_ID`, `FOOD_ID`),
    FOREIGN KEY (`ORDER_ID`) references `order`(`ORDER_ID`),
    FOREIGN KEY (`FOOD_ID`) references `food`(`FOOD_ID`)
);









-- -----------------------------------------------------
-- Create below: Table `Pro`.`order`
-- -----------------------------------------------------
CREATE TABLE `order` (
	`ORDER_ID` VARCHAR(10) NOT NULL,
    `RESTAURANT_ID` VARCHAR(10) NOT NULL,
    `CUSTOMER_ID` VARCHAR(32) NOT NULL,
    `ORDER_TIME` DATETIME NOT NULL,
    `ORDER_STATUS` VARCHAR(10) NOT NULL,
    `TABLE_ID` VARCHAR(10) NOT NULL,
    PRIMARY KEY (`ORDER_ID`),
     FOREIGN KEY (`CUSTOMER_ID`) references `customer`(`CUSTOMER_ID`),
     FOREIGN KEY (`TABLE_ID`) references `table`(`TABLE_ID`)
);









-- -----------------------------------------------------
-- Create below: Table `Pro`.`order_customer`
-- -----------------------------------------------------
CREATE TABLE `order_customer` (
	`ORDER_ID` VARCHAR(10) NOT NULL,
    `CUSTOMER_ID` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`ORDER_ID`, `CUSTOMER_ID`),
     FOREIGN KEY (`ORDER_ID`) references `order`(`ORDER_ID`),
     FOREIGN KEY (`CUSTOMER_ID`) references `customer`(`CUSTOMER_ID`)
);










-- -----------------------------------------------------
-- Create below: Table `Pro`.`customer`
-- -----------------------------------------------------
CREATE TABLE `customer` (
	`CUSTOMER_ID` VARCHAR(32) NOT NULL,
    `CUSTOMER_NAME` VARCHAR(10) NOT NULL,
    `PHONE_NUMBER` VARCHAR(20),
    `SEX` VARCHAR(10) NOT NULL,
    `BIRTH` VARCHAR(10) NOT NULL,
    `DISCOUNT_RATE` FLOAT,
    PRIMARY KEY (`CUSTOMER_ID`)
);









-- -----------------------------------------------------
-- Create below: Table `Pro`.`restaurant`
-- -----------------------------------------------------
CREATE TABLE `restaurant` (
	`RESTAURANT_ID` VARCHAR(10) NOT NULL,
    `RESTAURANT_NAME` VARCHAR(10) NOT NULL,
    `RESTAURANT_ADDRESS` VARCHAR(10) NOT NULL,
	`SALES` FLOAT NOT NULL,
    `LOGIN_NAME` VARCHAR(32) NOT NULL,
    `LOGIN_PASSWORD` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`RESTAURANT_ID`)
);










-- -----------------------------------------------------
-- Create below: Table `Pro`.`food`
-- -----------------------------------------------------
CREATE TABLE `food` (
	`FOOD_ID` VARCHAR(10) NOT NULL,
    `RESTAURANT_ID` VARCHAR(10) NOT NULL,
    `FOOD_TYPE` VARCHAR(20) NOT NULL,
    `FOOD_NAME` VARCHAR(20) NOT NULL,
    `PRICE` FLOAT NOT NULL,
    `INVENTORY` DECIMAL(3,0) NOT NULL,
    PRIMARY KEY (`FOOD_ID`, `RESTAURANT_ID`),
     FOREIGN KEY (`RESTAURANT_ID`) references `restaurant`(`RESTAURANT_ID`)
);









-- -----------------------------------------------------
-- Create below: Table `Pro`.`table`
-- -----------------------------------------------------
CREATE TABLE `table` (
	`TABLE_ID` VARCHAR(10) NOT NULL,
    `RESTAURANT_ID` VARCHAR(10) NOT NULL,
    `SEAT_NUMBER` DECIMAL(2,0) NOT NULL,
    `TABLE_STATUS` VARCHAR(10) NOT NULL,
    PRIMARY KEY (`TABLE_ID`, `RESTAURANT_ID`),
	 FOREIGN KEY (`RESTAURANT_ID`) references `restaurant`(`RESTAURANT_ID`)
);









-- -----------------------------------------------------
-- End of coding
-- -----------------------------------------------------


