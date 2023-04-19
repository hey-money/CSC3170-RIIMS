use riimages;
SELECT *
FROM `order_details`
LEFT JOIN `order`
ON `order_details`.ORDER_ID = `order`.ORDER_ID
LEFT JOIN `food`
ON `order_details`.FOOD_ID = `food`.FOOD_ID
where `order`.CUSTOMER_ID=1;
