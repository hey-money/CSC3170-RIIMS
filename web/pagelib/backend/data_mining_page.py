'''
page: dish data mining page
Author: Lai
Create Date: 2023.4.18
'''
import streamlit as st
import pandas as pd
import numpy as np

from utils import sql


def dish_data_mining_page():
    ##
    st.title("Dish Data Mining")
    