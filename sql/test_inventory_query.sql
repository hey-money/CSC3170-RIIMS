use riimages;

-- INSERT food(`RESTAURANT_ID`,`FOOD_TYPE`,`FOOD_NAME`,`PRICE`,`INVENTORY`) values(
--     114514, 'xue', 'yinbinjiu', 114514, 18);
-- INSERT food(`RESTAURANT_ID`,`FOOD_TYPE`,`FOOD_NAME`,`PRICE`,`INVENTORY`) values(
--     114514, 'xue', 'yinbinjiu2', 114, 51);

-- SELECT FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY
-- FROM food
-- where (RESTAURANT_ID = 1);

-- Update food
-- SET INVENTORY = 999
-- WHERE RESTAURANT_ID = 114514
-- AND FOOD_ID = 3;

-- Update food
-- SET PRICE = 999, FOOD_TYPE = '雪'
-- WHERE RESTAURANT_ID = 1
-- AND FOOD_ID = 1;


Update food SET PRICE = 1111 WHERE RESTAURANT_ID = 2 AND FOOD_ID = 54; 