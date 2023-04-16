'''
page: inventory management, just increase/decrease inventory numbers!
Author: Lai
Create Date: 2023.4.16
'''

import streamlit as st
import pandas as pd
import numpy as np

from utils import sql


def inventory_management_page():
    st.title("Inventory management")
    st.text("In this page, you can increase/decrease inventory quantities.")

    ## show inventory
    st.subheader("View Inventory Quantities")
    
    cnx, cursor = sql.create_session_cursor()
    result = sql.execute_fetchall(cursor, '''
    SELECT FOOD_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY
    FROM food
    where (RESTAURANT_ID = %s)
    ''', (st.session_state['RestaurantID'], ))
    cnx.close()

    df = pd.DataFrame(result)

    # update the column data type
    df = df.astype({4: int})
    # update the column name
    df.columns = ['FOOD ID', 'FOOD TYPE', 'FOOD NAME', 'PRICE', 'INVENTORY']

    st.table(df.style.bar(color='#FFFFB9', subset=['INVENTORY'], align='mid', vmin=0).set_precision(2))

    ## update inventory
    st.subheader("Update Inventory Quantities")

    # st.columns
    st.text('You may select food by ID/Name. Leave the other empty:')
    c1, c2 = st.columns(2)
    with c1:
        food_id = st.text_input("Food ID", placeholder="Enter the food ID you want to update")
    with c2:
        food_name = st.text_input("Or, Food name", placeholder="Enter the food name you want to update")
    
    new_quant = st.text_input("Food new quantity", placeholder="Enter the new quantity")
    # do update. Need to confirm that the dish REALLY belongs to that restaurant!!!

    if st.button('Update!'):
        if not food_id and not food_name: 
            st.warning('You may enter at least one of food name/id!')
        elif int(new_quant) < 0 or int(new_quant) > 999 or new_quant.find('.') != -1:
            st.warning('You new quantity is not valid!')
        else:
            # Do update.
            cnx, cursor = sql.create_session_cursor()
            if food_id:
                # by ID
                check_query = '''
                SELECT *
                FROM food
                WHERE RESTAURANT_ID = %s
                AND FOOD_ID = %s;
                '''
                query = """
                Update food
                SET INVENTORY = %s
                WHERE RESTAURANT_ID = %s
                AND FOOD_ID = %s;
                """
                content = (st.session_state['RestaurantID'], food_id)
            else:
                # by Name
                check_query = '''
                SELECT *
                FROM food
                WHERE RESTAURANT_ID = %s
                AND FOOD_NAME = %s;
                '''
                query = """
                Update food
                SET INVENTORY = %s
                WHERE RESTAURANT_ID = %s
                AND FOOD_NAME = %s;
                """
                content = (st.session_state['RestaurantID'], food_name)
            
            # Pre-check, see if exist!
            result = sql.execute_fetchone(cursor, check_query, content)

            if result:
                # ID/Name is valid!!
                success = sql.execute_command(cursor, cnx, query, (new_quant, st.session_state['RestaurantID'], food_id))
                if success:
                    st.success("Updated successfully! You may see changes on the table above!")
                    st.experimental_rerun()
                else:
                    st.warning('Update failed!')
            else:
                st.warning('Your food ID/Name is wrong!')

            cnx.close() 
    # st.button('Refresh')