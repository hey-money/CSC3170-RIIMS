'''
page: dish data mining page
Author: Lai
Create Date: 2023.4.18
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql

from pagelib.backend._analysis_page import(
    _fetch_foodorder_data,
    _process_dish_analysis
)

def dish_data_mining_page() -> None:
    ##
    st.title("Dish Data Mining")
    
    st.subheader("Frequent Selling Groups")



    st.subheader("Dish Sale Prediction")

    # fetch data
    result = _fetch_foodorder_data()
    # process data
    result = _process_dish_analysis(result, 'D')    

    dish = st.selectbox('Select a dish to predict:', result.columns)

    alg_select = st.radio('Prediction Methods:', 
             ['Linear Regression', 'ARMA (Will Support Later)'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

    st.line_chart(result[dish])

    # print(alg_select)
