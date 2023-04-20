use riimages;

SELECT `order`.`RESTAURANT_ID`,`order`.CUSTOMER_ID,`customer`.`PHONE_NUMBER`, MAX(ORDER_TIME) AS LAST_TIME
FROM `order`
LEFT JOIN `customer` ON  `order`.`CUSTOMER_ID`=`customer`.`CUSTOMER_ID`
where `order`.`RESTAURANT_ID`=1
GROUP BY CUSTOMER_ID;


