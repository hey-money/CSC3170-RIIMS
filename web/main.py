'''
Main streamlit script for the web app
Author: Lai
Create Date: 2023.4.14
'''
# python imports
import os

# pagkage imports
import streamlit as st
from streamlit_option_menu import option_menu as om

## component imports
# web pages
from pagelib.log_page import *
from pagelib.backend.summary_page import summary_page
from pagelib.backend.analysis_page import (
    turnover_analysis_page,
    dish_analysis_page,
    dish_data_mining_page
)
from pagelib.backend.membership_manage import membership_management_page
from pagelib.backend.inventory_manage import inventory_management_page
from pagelib.backend.dish_manage import dish_management_page

# utils & config
import webconfig as config
from utils import control as control_util


st.set_page_config(page_title=config.ProjName, page_icon='assets/online-library.png')


if "function" not in st.session_state: 
    # Log in for the first time
    st.session_state["function"] = "log" # RANGE in {log, backend}
if "RestaurantID" not in st.session_state: 
    # Log in for the first time
    st.session_state["RestaurantID"] = 0



# logging functions
if st.session_state["function"] == "log":
    c1, c2 = st.columns((1,3))
    with c1: 
        st.image("assets/logo1.png")
    with c2: 
        st.title("Restaurant Integrated Intelligent MAnaGEment System")

    # st.subheader('Restaurant Backend Login Panel')
    selected = om("RIIMAGES  Restaurant-side  Backend  Management  Panel", 
                    ["LOG IN", 'SIGN UP'], 
                menu_icon =  "chip_fill",
                icons=['house', 'text-indent-right'], 
                orientation='horizontal',
                default_index=0)
    if selected == "LOG IN":
        log_in_page()
    elif selected =="SIGN UP":
        sign_up_page()

# logged in! show the backend
elif st.session_state["function"] == "backend":
    with st.sidebar:
        st.image("assets/logo2.png")
        selected_c = om("Management panel", 
                        ["Summary", 
                         "Turnover Analysis",
                         "Dish Analysis",
                         "Dish Data Mining",
                         "Membership Analysis",
                         "Inventory Management",
                         "Dish Management"], 
                    menu_icon =  "None",
        # This icon need to be updated later!!
                    icons=['house', 'ui-checks','columns','text-indent-right','eye-fill','heptagon-half','ui-radios-grid'], 
                    default_index=0)
        st.sidebar.info(
                """
            Welcome to RIIMAGES Restaurant-side Backend Management Panel! Contact us with +11 45141919810.  
            
            Copyright © 2023 RIIMAGES Restaurant Integrated Intelligent MAnaGEment System
                """
        )
    if selected_c == "Summary":
        summary_page()
    elif selected_c == "Turnover Analysis":
        turnover_analysis_page()
    elif selected_c == "Dish Analysis":
        dish_analysis_page()
    elif selected_c == "Dish Data Mining":
        dish_data_mining_page()
    elif selected_c == "Membership Analysis":
        membership_management_page()      
    elif selected_c == "Inventory Management":
        inventory_management_page()
    elif selected_c == "Dish Management":
        dish_management_page()

    st.markdown('#')
    st.markdown('#')
    st.text("Log out the account by the button below:")
    st.button("Log out", on_click=control_util.move_to_log_state)

