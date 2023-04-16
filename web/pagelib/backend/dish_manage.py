'''
page: dish management, can add/delete/find/update specific dishes!
Author: Lai
Create Date: 2023.4.16
'''

import streamlit as st
import pandas as pd
import numpy as np

from utils import sql
from streamlit_option_menu import option_menu as om


def dish_management_page():
    st.title("Dish management")
    st.text("In this page, you can view/add/remove/update specific dishes!.")

    ##
    st.subheader("View dishes")
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

    st.dataframe(df.style.set_precision(2), use_container_width = True, height=(min(len(df), 15) + 1) * 35 + 3)

    st.subheader("Make changes")

    selected = om("Integrated  Dish  Management  Panel", 
                    ["Add a dish", "Remove a dish", "Update a dish"], 
                menu_icon =  "balloon",
                icons=['bag-plus', 'backspace', 'clipboard-check'], 
                orientation='horizontal',
                default_index=0)
    if selected == "Add a dish":
        add_dish_section()
    elif selected =="Remove a dish":
        remove_dish_section()
    elif selected =="Update a dish":
        update_dish_section()


def add_dish_section():
    ##
    food_type = st.text_input("Food Type", placeholder="Enter the food type")
    food_name = st.text_input("Food Name", placeholder="Enter the food name")
    food_price = st.text_input("Food Price", placeholder="Enter the food price")
    food_inventory = st.text_input("Initial inventory", placeholder="Enter the initial inventory")

    st.text("The effects will appear as soon as you click the button.")

    if st.button('Add!'):
        if not food_type or not food_name or not food_price or not food_inventory:
            st.warning('All input boxes should not be empty!')
        else:
            cnx, cursor = sql.create_session_cursor()
            query = """
            INSERT INTO food (RESTAURANT_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY)
            VALUES (%s, %s, %s, %s, %s)
            """
            success = sql.execute_command(cursor, cnx, query, (st.session_state['RestaurantID'],
                                                               food_type, food_name, food_price, food_inventory))
            cnx.close()
            if success:
                st.success("Add a dish - seccessfully!")
                st.experimental_rerun()
            else:
                st.warning('Add a dish - failed!')


def remove_dish_section():
    ##
    food_id = st.text_input("Food ID", placeholder="Enter the food ID")

    st.text("The effects will appear as soon as you click the button.")
    if st.button('Remove!'):
        if not food_id:
            st.warning('All input boxes should not be empty!')
        else:
            cnx, cursor = sql.create_session_cursor()

            check_query = '''
            SELECT *
            FROM food
            WHERE RESTAURANT_ID = %s
            AND FOOD_ID = %s;
            '''
            query = """
            DELETE from food
            WHERE RESTAURANT_ID = %s
            AND FOOD_ID = %s;
            """
            content = (st.session_state['RestaurantID'], food_id)
            
            # Pre-check, see if exist!
            result = sql.execute_fetchone(cursor, check_query, content)

            if result:
                # ID is valid!!
                success = sql.execute_command(cursor, cnx, query, content)
                cnx.close() 
                if success:
                    st.success("Remove successfully! You may see changes on the table above!")
                    st.experimental_rerun()
                else:
                    st.warning('Remove failed!')
            else:
                st.warning('Your food ID is wrong!')


def update_dish_section():
    ##
    # st.columns
    st.text('You may select a food by ID first:')
    food_id = st.text_input("Food ID", placeholder="Enter the food ID you want to update")
    
    st.text('Change the inventory at Inventory management panel.')
    c1, c2, c3 = st.columns(3)

    with c1:
        food_type = st.text_input("Food type", placeholder="Fill this if you want to update")
    with c2:
        food_name = st.text_input("Food name", placeholder="Fill this if you want to update")
    with c3:
        food_price = st.text_input("Food Price", placeholder="Fill this if you want to update")


    st.text("The effects will appear as soon as you click the button.")

    if st.button('Update!'):
        if not food_id and (not food_name and not food_price and not food_type): 
            st.warning('You may enter food id, and at least one of food name/price!')
        else:
            # Do update.
            cnx, cursor = sql.create_session_cursor()
            check_query = '''
            SELECT *
            FROM food
            WHERE RESTAURANT_ID = %s
            AND FOOD_ID = %s;
            '''
            query_prefix = '''
            Update food 
            SET '''
            query_postfix = ''' 
            WHERE RESTAURANT_ID = %s 
            AND FOOD_ID = %s;
            '''
            result = sql.execute_fetchone(cursor, check_query, (st.session_state['RestaurantID'], food_id))

            if result:
                # ID is valid!!
                query_middle = []
                content = []
                if food_type:
                    query_middle.append(' FOOD_TYPE = %s ')
                    content.append(food_type)
                if food_name:
                    query_middle.append(' FOOD_NAME = %s ')
                    content.append(food_name)                
                if food_price:
                    query_middle.append(' PRICE = %s ')
                    content.append(food_price)

                success = sql.execute_command(cursor, cnx, query_prefix+
                                              ','.join(query_middle)+query_postfix, 
                                              tuple(content)+(st.session_state['RestaurantID'], food_id))
                cnx.close() 
                if success:
                    st.success("Updated successfully! You may see changes on the table above!")
                    st.experimental_rerun()
                else:
                    st.warning('Update failed!')
            else:
                st.warning('Your food ID is wrong!')

    # st.button('Refresh')
