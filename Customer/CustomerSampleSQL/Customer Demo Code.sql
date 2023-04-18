-- Customer Demo Code

-- Customer Account Registration
INSERT INTO customer (CUSTOMER_ID, CUSTOMER_NAME, PHONE_NUMBER, SEX, BIRTH) 
VALUES (114514, "Yaju Senpai", "81-1919810", 0, 19190810)

-- Show Visible Food
SELECT 
    *
FROM
    food
WHERE
	VISIBLE = 1

-- Update Table Status before meal
UPDATE `table` 
SET 
    TABLE_STATUS = 1
WHERE
    TABLE_ID = 1;

-- Place an order
INSERT INTO order_details (ORDER_ID, FOOD_ID, QUANTITY) 
VALUES (3000, 2, 1), (3000, 1, 2);

-- Update Food inventory
UPDATE food
SET 
    INVENTORY = INVENTORY-1
WHERE
    FOOD_ID = 1;

-- Update Table Status after meal
UPDATE `table` 
SET 
    TABLE_STATUS = 1
WHERE
    TABLE_ID = 1;

