-- Demo code for data mining use



-- Get one customer's all orders
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



-- Get all visited customer's last visit time
SELECT `order`.`RESTAURANT_ID`,`order`.CUSTOMER_ID,`customer`.`PHONE_NUMBER`, MAX(ORDER_TIME) AS LAST_TIME
FROM `order`
LEFT JOIN `customer` ON  `order`.`CUSTOMER_ID`=`customer`.`CUSTOMER_ID`
where `order`.`RESTAURANT_ID`=1
GROUP BY CUSTOMER_ID;
