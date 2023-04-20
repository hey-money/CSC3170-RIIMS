use riimages;
SELECT `order`.CUSTOMER_ID ,`order`.ORDER_ID,`order`.`ORDER_TIME`,
    `order`.RESTAURANT_ID, `order`.`TABLE_ID`,`food`.FOOD_ID,`food`.FOOD_TYPE,
    `food`.FOOD_NAME,`food`.PRICE,`order_details`.QUANTITY,`food`.`VISIBLE`,
    `food`.`INVENTORY`
FROM `order_details` 
LEFT JOIN `order` 
ON `order_details`.ORDER_ID = `order`.ORDER_ID 
LEFT JOIN `food`
ON `order_details`.FOOD_ID = `food`.FOOD_ID
where `order`.CUSTOMER_ID=1;