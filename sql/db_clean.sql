use `riimages`;

SET @OLD_SAFE_UPDATES=@@sql_safe_updates;
SET @OLD_FOREIGN_KEY_CHECKS=@@foreign_key_checks;
SET SQL_SAFE_UPDATES = 0;
SET FOREIGN_KEY_CHECKS = 0;

delete from signup_records;

delete from `restaurant`;

delete from `food`;

delete from `order`;

delete from `order_details`;

delete from `table`;

delete from `customer`;





SET SQL_SAFE_UPDATES = @OLD_SAFE_UPDATES;
SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS;