'''
page: analysis page processing functions
Author: Lai
Create Date: 2023.4.18
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql


def _fetch_foodorder_data() -> pd.DataFrame:
    cnx, cursor = sql.create_session_cursor()
    query = '''
    SELECT od.order_id, od.food_id, food_name, food_type, quantity, price, order_time from 
    order_details od inner join food inner join `order`
    ON od.food_id = food.food_id AND od.order_id = `order`.order_id
    WHERE od.order_id in (
        select order_id from `order` where restaurant_id = %s
    );
    '''
    result = sql.execute_fetchall(cursor, query, (st.session_state['RestaurantID'],) )
    result = pd.DataFrame(result)

    # process data
    result.columns = ['ORDER_ID', 'FOOD_ID', 'FOOD_NAME', 'FOOD_TYPE', 'QUANTITY', 'PRICE', 'ORDER_TIME']
    result = result.astype({'QUANTITY': int})
    return result


def _process_overturn_analysis(df: pd.DataFrame, viewmode='D') -> pd.DataFrame:
    ''' Processing for the overturn analysis. This function receives food order, then:
        1. Calculate the price * quantity
        2. Group by FOOD_TYPE
        3. Group by date (with viewmode)
    '''
    # step 1
    df['Money'] = df['QUANTITY'] * df['PRICE']
    # step 2
    ans = pd.DataFrame()
    df1 = df.groupby('FOOD_TYPE')
    for food_type, sub_df in df1:
        # step 3
        date_grouped = sub_df.groupby(pd.Grouper(key='ORDER_TIME', axis=0, freq=viewmode)).sum(numeric_only=True)
        ans[food_type] = date_grouped['Money']
    ans.index = [ans.index[i].to_pydatetime().strftime('%Y-%m-%d') for i in range(len(ans.index))]
    return ans


def _process_dish_analysis(df: pd.DataFrame, viewmode='D') -> pd.DataFrame:
    ''' Processing for the overturn analysis. This function receives food order,
        Then group by food name and date respectively.
    '''
    ans = pd.DataFrame()
    df1 = df.groupby('FOOD_NAME')
    for food_name, sub_df in df1:
        date_grouped = sub_df.groupby(pd.Grouper(key='ORDER_TIME', axis=0, freq=viewmode)).sum(numeric_only=True)
        ans[food_name] = date_grouped['QUANTITY']
    ans.index = [ans.index[i].to_pydatetime().strftime('%Y-%m-%d') for i in range(len(ans.index))]
    return ans


