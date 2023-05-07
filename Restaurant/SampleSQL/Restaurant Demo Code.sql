-- Restaurant CRUD Demo Code

-- Login check with one specific account
SELECT RESTAURANT_ID, RESTAURANT_NAME
FROM restaurant
where (LOGIN_NAME = 'Lv Cha') AND (LOGIN_PASSWORD = '123456')


-- Sign up with some specific information
INSERT INTO signup_records (FIRST_NAME, LAST_NAME, PHONE_NUMBER, COUNTRY_NAME, 
PROVINCE_NAME, STREET_ADDRESS, ACCOUNT_PASSWORD, EMAIL_ADDRESS, ACCOUNT_NAME)
VALUES ('Yangsheng', 'Zhu', '1111111', 'China', 'Guangdong', 'Longxiang Ave. 2001', '123456', 'xxx@yy.edu', 'gzs')


-- Create a new dish
INSERT INTO food (RESTAURANT_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY)
VALUES (1, 'meat', 'Roast Pork', 28, 99)


-- Update visibility (Remove a dish)
UPDATE food SET VISIBLE = 0 WHERE RESTAURANT_ID = 1 AND FOOD_ID = 11


-- Update food metadata (e.g., name, price...)
-- Though the effect is "Update", we use "Insert" here. See the content for explanation
INSERT INTO food (RESTAURANT_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY)
VALUES (1, 'meat', 'Roast Pork', 28, 99)            


-- Update food inventory
Update food
SET INVENTORY = 110
WHERE RESTAURANT_ID = 1 AND FOOD_NAME = 'Roast Pork' AND VISIBLE = 1;

