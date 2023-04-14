import streamlit as st

def move_to_backend_state():
    st.session_state["function"] = "backend"

def move_to_log_state():
    st.session_state["function"] = "log"
    st.session_state.pop("RestaurantName")
    st.session_state["RestaurantID"] = 0

