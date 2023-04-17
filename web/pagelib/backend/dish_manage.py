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

    mode = st.radio("Display Mode", ('View Unhide Only', 'View ALL'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    cnx, cursor = sql.create_session_cursor()
    if mode == 'View Unhide Only':
        # only shown unhide
        query = '''SELECT FOOD_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY
        FROM food
        where (RESTAURANT_ID = %s)
        AND VISIBLE = 1
        '''
    else:
        query = '''SELECT VISIBLE, FOOD_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY
        FROM food
        where (RESTAURANT_ID = %s)
        '''

    result = sql.execute_fetchall(cursor, query, (st.session_state['RestaurantID'], ))
    cnx.close()

    df = pd.DataFrame(result)

    # update the column name
    if mode == 'View Unhide Only':
        df.columns = ['FOOD ID', 'FOOD TYPE', 'FOOD NAME', 'PRICE', 'INVENTORY']
    else:
        df.columns = ['VISIBLE', 'FOOD ID', 'FOOD TYPE', 'FOOD NAME', 'PRICE', 'INVENTORY']
        df['VISIBLE'] = df['VISIBLE'].apply(lambda x: '✅' if x == 1 else '❌')
    st.dataframe(df.style.format(precision=2), use_container_width = True, height=(min(len(df), 15) + 1) * 35 + 3)

    st.subheader("Make changes")

    selected = om("Integrated  Dish  Management  Panel", 
                    ["Add a dish", "Hide/Unhide a dish", "Update a dish"], 
                menu_icon =  "balloon",
                icons=['bag-plus', 'eye', 'clipboard-check'], 
                orientation='horizontal',
                default_index=0)
    if selected == "Add a dish":
        add_dish_section()
    elif selected =="Hide/Unhide a dish":
        hide_dish_section()
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


def hide_dish_section():
    ##
    food_id = st.text_input("Food ID", placeholder="Enter the food ID")

    st.text("The effects will appear as soon as you click the button.")
    c1, c2 = st.columns(2)
    with c1:
        st.button('Hide!', on_click=hide_unhide_callback, args=(food_id, True))

    with c2:
        st.button('Unhide!', on_click=hide_unhide_callback, args=(food_id, False))

def hide_unhide_callback(food_id, do_hide):
    ## 
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
        query_hide = """
        UPDATE food SET VISIBLE = 0 WHERE RESTAURANT_ID = %s AND FOOD_ID = %s
        """
        query_unhide = """
        UPDATE food SET VISIBLE = 1 WHERE RESTAURANT_ID = %s AND FOOD_ID = %s
        """
        content = (st.session_state['RestaurantID'], food_id)
        
        # Pre-check, see if exist!
        result = sql.execute_fetchone(cursor, check_query, content)

        if result:
            # ID is valid!!
            if do_hide:
                success = sql.execute_command(cursor, cnx, query_hide, content)
            else:
                success = sql.execute_command(cursor, cnx, query_unhide, content)

            cnx.close() 
            if success:
                st.success("Hide/unhide successfully! You may see changes on the table above!")
                # st.experimental_rerun()
            else:
                st.warning('Hide/unhide failed!')
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
            # query_prefix = '''
            # Update food 
            # SET '''
            # query_postfix = ''' 
            # WHERE RESTAURANT_ID = %s 
            # AND FOOD_ID = %s;
            # '''
            query = '''
            INSERT INTO food (RESTAURANT_ID, FOOD_TYPE, FOOD_NAME, PRICE, INVENTORY)
            VALUES (%s, %s, %s, %s, %s)            
            '''
            result = sql.execute_fetchone(cursor, check_query, (st.session_state['RestaurantID'], food_id))
            if result:
                # ID is valid!!
                # 1. make the original invisible
                success = sql.execute_command(cursor, cnx, '''
                UPDATE food SET VISIBLE = 0 WHERE FOOD_ID = %s
                ''', (food_id, ))
                if success:
                    print('set invisiable!')

                # 2. create a new food entity
                result = list(result)
                print('result:', result)
                if food_type:
                    result[2] = food_type
                if food_name:
                    result[3] = food_name
                if food_price:
                    result[4] = food_price

                success = sql.execute_command(cursor, cnx, 
                                              query, result[1:5]+result[6:])
                cnx.close() 
                if success:
                    st.success("Updated successfully! You may see changes on the table above!")
                    st.experimental_rerun()
                else:
                    st.warning('Update failed!')
            else:
                st.warning('Your food ID is wrong!')

    # st.button('Refresh')
