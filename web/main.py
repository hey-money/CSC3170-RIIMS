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
from pagelib.log_page import *
# component imports
import webconfig as config



st.set_page_config(page_title=config.ProjName)


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
    selected = om("RIIMAGES Restaurant-side Backend Management Panel", 
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
        st.image("assets/logo1.png")
        selected_c = om("Management panel", 
                        ["Introduction", 
                         "Shopping Cart",
                         "Current Order"], 
                    menu_icon =  "None",
                    icons=['house', 'ui-checks','columns','text-indent-right','ui-radios-grid','heptagon-half','eye-fill'], 
                    default_index=0)
        st.sidebar.info(
                """
            Welcome to chipandas! Contact us with +86 17767361813.  
            Copyright © 2022 CHIPANDAS Campany Limited
                """
        )
    if selected_c == "Introduction":
        # preview_page()
        ...
    elif selected_c == "Shopping Cart":
        # shopping_cart_page()
        ...
    elif selected_c == "Current Order":
        ...
        # custormer_order_page()
    st.button("Log out", on_click=move_to_log_state)

