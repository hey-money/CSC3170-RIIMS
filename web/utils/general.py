'''
General use utilities
Author: Lai
Create Date: 2023.4.16
'''
import time
import base64
import streamlit as st

def log_string(content: str):
    ''' Log a string to console with time format. '''
    print(f'[INFO] {time.ctime()}: {content}')


def log_catch_error(content: str):
    ''' Log a string to console with time format. '''
    print(f'[ERROR] {time.ctime()}: {content}')


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
