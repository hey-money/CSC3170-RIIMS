'''
page: membership_management
Author: Lai
Create Date: 2023.4.16
'''
import streamlit as st
import pandas as pd
import numpy as np
import datetime

import time
from utils import sql


def foo():
    st.text("Under construction!!!")

def membership_management_page() -> None:
    ##
    st.title("Membership Management")

    cnx, cursor = sql.create_session_cursor()

    query = '''
    SELECT `order`.CUSTOMER_ID,`customer`.`PHONE_NUMBER`, 
    `customer`.`CUSTOMER_NAME`, `customer`.`SEX`, MAX(ORDER_TIME) AS LAST_TIME
    FROM `order`
    LEFT JOIN `customer` ON  `order`.`CUSTOMER_ID`=`customer`.`CUSTOMER_ID`
    where `order`.`RESTAURANT_ID`=%s
    GROUP BY CUSTOMER_ID;
    '''
    result = sql.execute_fetchall(cursor, query, (st.session_state['RestaurantID'], ))
    cnx.close()
    result = pd.DataFrame(result)
    result.columns = ['CUSTOMER_ID', 'PHONE_NUMBER', 'NAME', 'SEX', 'LAST_VISIT']
    result.insert(1, 'CUSTOMER_NAME', (result['NAME']+result['SEX']).values)
    result['CUSTOMER_NAME'] = result['CUSTOMER_NAME'].apply(
        lambda x: x[:-1].rstrip('*') + ('先生' if x[-1]=='男' else '女士'))
    result = result.drop(columns=['NAME', 'SEX'])
 
    st.text(f'You have {len(result)} customers!')
    st.dataframe(result, use_container_width=True, height=(min(len(result), 12) + 1) * 35 + 3)

    st.subheader('Coupons AutoSend')

    days = st.slider('Send Coupons to customers who havn\'t visit for days:', 0, 14, 7)

    discount_rate = st.slider('Coupons Discount Rate:', 0.5, 1., 0.88)

    now = datetime.datetime(year=2023, month=3, day=15)

    result_coupon = result.loc[result['LAST_VISIT'] < now - datetime.timedelta(days=days)]
    
    st.text(f'You have {len(result_coupon)} customers satisfied the condition!')
    st.dataframe(result_coupon, use_container_width=True, height=(min(len(result), 12) + 1) * 35 + 3)

    if st.button('Send Coupons!'):
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)        
        for i in range(100):
            time.sleep(np.random.rand()*0.006)
            my_bar.progress(i+1, text=progress_text)
        st.success('Send coupons to Wechat / Zhifubao successfully!')

