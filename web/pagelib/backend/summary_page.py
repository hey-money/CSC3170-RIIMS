'''
page: summarization
Author: Lai
Create Date: 2023.4.16
'''
import streamlit as st


def summary_page():
    st.title('General Sales Summary')
    st.text(f'You are logging as: {st.session_state["RestaurantName"]}')

    # General metrics
    st.subheader("Overall statistics")

    col1, col2, col3 = st.columns(3)
    col1.metric("Orders", "114", "+5%")
    col2.metric("Customers", "514", "-8%")
    col3.metric("Turnover", f"$ {1919}", "8%")


    st.subheader("Sales trend")

    st.text('Under construction...')


    st.subheader("Best selling dish")

    st.text('Under construction...')


    st.subheader("Inventory statistics")

    st.text('Under construction...')
