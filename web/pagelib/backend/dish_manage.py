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

    st.dataframe(df.style.set_precision(2), use_container_width = True)

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

    if st.button('Add!'):
        if not food_type or not food_name or not food_price or not food_inventory:
            st.warning('All input boxes should not be empty!')
        else:
            cnx, cursor = sql.create_session_cursor()
            query = """
            INSERT INTO food (RESTAURANT_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY)
            VALUES (%s, %s, %s, %s, %s)
            """
            success = sql.execute_command(cursor, cnx, query, (st.session_state['RestaurantID']))
            cnx.close()
            if success:
                st.success("Add a dish - seccessfully!")
            else:
                st.warning('Add a dish - failed!')
def remove_dish_section():
    ##
    st.subheader("Remove a dish")

def update_dish_section():
    ##
    st.subheader("Update a dish")

