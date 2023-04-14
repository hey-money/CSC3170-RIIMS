import streamlit as st

def move_to_backend_state():
    st.session_state["function"] = "backend"

def move_to_log_state():
    st.session_state["function"] = "log"

