'''
page: data visualization & analysis
Author: Lai
Create Date: 2023.4.16
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql
from pagelib.backend._analysis_page import (
    _fetch_foodorder_data, 
    _process_dish_analysis, 
    _process_overturn_analysis
)


def foo():
    st.text("Under construction!!!")


def turnover_analysis_page():
    ##
    st.title("Turnover Analysis")

    # get the view mode
    viewmode = st.radio("View Mode", ('1 Day', '3 Days', '1 Week', '1 Month'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    
    # fetch data
    result = _fetch_foodorder_data()

    # process data
    viewmode_map = {'1 Day': '1D', '3 Days': '3D', '1 Week': '7D', '1 Month': 'M'}
    result = _process_overturn_analysis(result, viewmode_map[viewmode])

    # show the data
    chart_data = pd.DataFrame(result)
    st.bar_chart(chart_data)


def dish_analysis_page():
    ##
    st.title("Dish Analysis")

    # fetch data
    result = _fetch_foodorder_data()
    # process data
    result = _process_dish_analysis(result, 'D')    

    # get the dish want to view
    options = st.multiselect(
        'Please enter the dishes you want to inspect:',
        result.columns, list(result.columns)[:2])

    if len(options) != 0:
        # show the data
        st.line_chart(result[options])
    else:
        st.warning('Please select at least one dish!')



