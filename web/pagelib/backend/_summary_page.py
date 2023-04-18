'''
page: summary page processing functions
Author: Lai
Create Date: 2023.4.18
'''
import streamlit as st
import pandas as pd
import numpy as np
import datetime

from utils import sql


def _fetch_order_data():
    cnx, cursor = sql.create_session_cursor()
    query = '''
    select order_id, order_time 
    from `order` 
    where RESTAURANT_ID=%s;
    '''
    result = sql.execute_fetchall(cursor, query, (st.session_state['RestaurantID'],) )
    result = pd.DataFrame(result)

    # process data
    result.columns = ['ORDER_ID', 'ORDER_TIME']
    # result = result.astype({'QUANTITY': int})
    return result



def _fetch_food_data():
    cnx, cursor = sql.create_session_cursor()

    query = '''
    SELECT * from food;
    '''

    food = sql.execute_fetchall(cursor, query, tuple())
    food = pd.DataFrame(food)[[0, 3]]
    food.index = food[0]
    food.columns = ['FOOD_ID', 'FOOD_NAME']
    return food    


def _get_range_turnover(df, start_date, end_date):
    ''' Get turnover at a specific range. '''
    df['Money'] = df['QUANTITY'] * df['PRICE']
    mask = (df['ORDER_TIME'] > start_date) & (df['ORDER_TIME'] < end_date)
    return df.loc[mask]['Money'].sum()


def _get_range_orders(df, start_date, end_date):
    ''' Get turnover at a specific range. '''
    mask = (df['ORDER_TIME'] > start_date) & (df['ORDER_TIME'] < end_date)
    df = df.drop_duplicates(subset=['ORDER_ID'])
    return df.loc[mask]['ORDER_ID'].count()


def _get_range_dishes(df, start_date, end_date):
    mask = (df['ORDER_TIME'] > start_date) & (df['ORDER_TIME'] < end_date)
    return df.loc[mask]['ORDER_ID'].count()


def _process_turnover_analysis(df, viewmode='D'):
    ''' Processing for the overturn analysis. This function receives food order, then:
        1. Calculate the price * quantity
        2. Group by date (with viewmode)
    '''
    # step 1
    df['Money'] = df['QUANTITY'] * df['PRICE']
    # step 2
    ans = df.groupby(pd.Grouper(key='ORDER_TIME', axis=0, freq=viewmode))['Money'].sum(numeric_only=True)
    ans.index = [ans.index[i].to_pydatetime().strftime('%Y-%m-%d') for i in range(len(ans.index))]
    return ans


def _get_best_selling_dish(orderfood, food, best_n=3):
    ''' Get the `best_n` selling dishes. '''
    best_n = min(best_n, 3)
    retval = pd.DataFrame(
        orderfood.groupby('FOOD_ID')
        .count()
        .sort_values(by=['ORDER_ID'], ascending=False)
        .head(best_n)['ORDER_ID']
    )
    retval = retval.rename(columns={'ORDER_ID': 'SELLING'})
    food_name = food.loc[retval.index, 'FOOD_NAME']
    retval['FOOD_NAME'] = food_name

    return retval

