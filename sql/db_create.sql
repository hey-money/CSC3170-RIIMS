SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP SCHEMA IF EXISTS `RIIMAGES` ;
CREATE SCHEMA IF NOT EXISTS `RIIMAGES` DEFAULT CHARACTER SET utf8 ;
USE `RIIMAGES` ;

-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`order_details`
-- -----------------------------------------------------
CREATE TABLE `order_details` (
	`ORDER_ID` INT NOT NULL,
    `FOOD_ID` INT NOT NULL,
    `QUANTITY` DECIMAL(3,0) NOT NULL,
    PRIMARY KEY (`ORDER_ID`, `FOOD_ID`),
    FOREIGN KEY (`ORDER_ID`) references `order`(`ORDER_ID`),
    FOREIGN KEY (`FOOD_ID`) references `food`(`FOOD_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`order`
-- -----------------------------------------------------
CREATE TABLE `order` (
	`ORDER_ID` INT NOT NULL AUTO_INCREMENT,
    `RESTAURANT_ID` INT NOT NULL,
    `CUSTOMER_ID` INT NOT NULL,
    `ORDER_TIME` DATETIME NOT NULL,
    -- `ORDER_STATUS` INT NOT NULL DEFAULT 1,
    `TABLE_ID` INT NOT NULL,
    PRIMARY KEY (`ORDER_ID`),
    FOREIGN KEY (`CUSTOMER_ID`) references `customer`(`CUSTOMER_ID`),
    FOREIGN KEY (`TABLE_ID`) references `table`(`TABLE_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`order_customer`
-- -----------------------------------------------------
CREATE TABLE `order_customer` (
	`ORDER_ID` INT NOT NULL,
    `CUSTOMER_ID`INT NOT NULL,
    PRIMARY KEY (`ORDER_ID`, `CUSTOMER_ID`),
    FOREIGN KEY (`ORDER_ID`) references `order`(`ORDER_ID`),
    FOREIGN KEY (`CUSTOMER_ID`) references `customer`(`CUSTOMER_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`customer`
-- -----------------------------------------------------
CREATE TABLE `customer` (
	`CUSTOMER_ID` INT NOT NULL AUTO_INCREMENT,
    `CUSTOMER_NAME` VARCHAR(50) NOT NULL,
    `PHONE_NUMBER` VARCHAR(20) NOT NULL,
    `SEX` INT NOT NULL,
    `BIRTH` VARCHAR(20) NOT NULL,
    `DISCOUNT_RATE` FLOAT,
    PRIMARY KEY (`CUSTOMER_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`restaurant`
-- -----------------------------------------------------
CREATE TABLE `restaurant` (
	`RESTAURANT_ID` INT NOT NULL AUTO_INCREMENT,
    `RESTAURANT_NAME` VARCHAR(50) NOT NULL,
    `RESTAURANT_ADDRESS` VARCHAR(50) NOT NULL,
	`SALES` FLOAT NOT NULL,
    `LOGIN_NAME` VARCHAR(32) NOT NULL,
    `LOGIN_PASSWORD` VARCHAR(32) NOT NULL,
    PRIMARY KEY (`RESTAURANT_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`food`
-- -----------------------------------------------------
CREATE TABLE `food` (
	`FOOD_ID` INT NOT NULL AUTO_INCREMENT,
    `RESTAURANT_ID` INT NOT NULL,
    `FOOD_TYPE` VARCHAR(20) NOT NULL,
    `FOOD_NAME` VARCHAR(20) NOT NULL,
    `PRICE` FLOAT NOT NULL,
    `VISIBLE` INT DEFAULT 1, 
    `INVENTORY` DECIMAL(3,0) NOT NULL,
    PRIMARY KEY (`FOOD_ID`, `RESTAURANT_ID`),
    FOREIGN KEY (`RESTAURANT_ID`) references `restaurant`(`RESTAURANT_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`table`
-- -----------------------------------------------------
CREATE TABLE `table` (
	`TABLE_ID` INT NOT NULL AUTO_INCREMENT,
    `RESTAURANT_ID` INT NOT NULL,
    `SEAT_NUMBER` DECIMAL(2,0) NOT NULL,
    `TABLE_STATUS` INT NOT NULL,
    PRIMARY KEY (`TABLE_ID`, `RESTAURANT_ID`),
	 FOREIGN KEY (`RESTAURANT_ID`) references `restaurant`(`RESTAURANT_ID`)
);


-- -----------------------------------------------------
-- Create below: Table `RIIMAGES`.`signup_records`
-- -----------------------------------------------------
CREATE TABLE `signup_records` (
	`RECORD_ID` INT NOT NULL AUTO_INCREMENT,
	`FIRST_NAME` VARCHAR(20) NOT NULL,
    `LAST_NAME` VARCHAR(20) NOT NULL,
    `PHONE_NUMBER` VARCHAR(20) NOT NULL,
    `COUNTRY_NAME` VARCHAR(20) NOT NULL,
	`PROVINCE_NAME` VARCHAR(20),
    `STREET_ADDRESS` VARCHAR(50) NOT NULL,
    `ACCOUNT_PASSWORD` VARCHAR(32) NOT NULL,
    `EMAIL_ADDRESS` VARCHAR(30) NOT NULL,
    `ACCOUNT_NAME` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`RECORD_ID`)
);


-- -----------------------------------------------------
-- End of coding
-- -----------------------------------------------------
