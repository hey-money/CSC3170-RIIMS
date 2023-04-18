'''
page: data visualization & analysis
Author: Lai
Create Date: 2023.4.16
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql


def foo():
    st.text("Under construction!!!")

def turnover_analysis_page():
    ##
    st.title("Turnover Analysis")

    viewmode = st.radio("View Mode", ('Day', 'Week', 'Month'))
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    # fetch data

    # show the data
    chart_data = pd.DataFrame(
        np.random.rand(50, 3) * 10,
        columns = ["a", "b", "c"])
    st.bar_chart(chart_data)


def dish_analysis_page():
    ##
    st.title("Dish Analysis")
    
    options = st.multiselect(
        'Please enter the dishes you want to inspect:',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])
    # fetch data

    # show the data
    chart_data = pd.DataFrame(
        np.random.randn(20, len(options)),
        columns=options)

    st.line_chart(chart_data)

    st.text(f'You selected: {options}')

def dish_data_mining_page():
    ##
    st.title("Dish Data Mining")
    foo()   

