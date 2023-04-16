import streamlit as st
import mysql.connector
import pandas as pd

from utils import control as control_util
from utils import general as general_util
from utils import sql

def authorize_login(name, password):

    cnx, cursor = sql.create_session_cursor()

    result = sql.execute_fetchone(cursor, '''
    SELECT RESTAURANT_ID, RESTAURANT_NAME
    FROM restaurant
    where (LOGIN_NAME = %s)
    AND (LOGIN_PASSWORD = %s)
    ''', (name, password))

    cnx.close()

    general_util.log_string(f'login query result: {result}')

    ### code for real use ###
    # if result:
    #     ID = result[0]
    #     Name = result[1]
    # else:
    #     ID = None

    ### code for fake use ###
    ID = 114514  
    Name = 'Kuai Le Shi Jian'

    if ID is None:
        st.warning("Invalid Login Information! Please Recheck Your Input!")
    else:
        control_util.move_to_backend_state()
        if "RestaurantID" not in st.session_state: 
            st.session_state["RestaurantID"] = 0
        st.session_state["RestaurantID"] = ID
        st.session_state["RestaurantName"] = Name

    
def log_in_page():
    st.text("Please login here.")
    login_name = st.text_input("Restaurant name", placeholder="keep empty and login!")
    login_password = st.text_input("Password", placeholder="keep empty and login!")

    st.button("Log In!", on_click=authorize_login, args=(login_name, login_password))


def sign_up_page():
    st.text("Please leave your information here.")
    st.text("Our sales manager will contact you later to sign the contract.")
    st.text("Then, your restaurant account will be created.")


    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    phone_number = st.text_input("Phone Number")
    email_address = st.text_input("Email Address")

    # Create a selectbox for countries
    country_name = st.selectbox("Select your country:", ['China', 'International'])
    # Create a selectbox for provinces
    if country_name == "China":
        province_options =  ["Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei", "Heilongjiang", "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Inner Mongolia", "Ningxia", "Qinghai", "Shaanxi", "Shandong", "Shanghai", 
                        "Shanxi", "Sichuan", "Tianjin", "Tibet", "Xinjiang", "Yunnan", "Zhejiang", "Taiwan", "Hong Kong", "Macau"]
        province = st.selectbox("Select a province:", province_options)
    else:
        province = None

    street_address = st.text_input("Street Address")

    login_name = st.text_input("Account login name") 
    password = st.text_input("Account login password")

    if st.button("Sign Up"):
        if not first_name or not last_name or not phone_number or not email_address or not country_name\
                or not street_address or not login_name or not password:
            st.warning('All input boxes should not be empty!')

        else:
            cnx, cursor = sql.create_session_cursor()
            query = """
            INSERT INTO signup_records (FIRST_NAME, LAST_NAME, PHONE_NUMBER, COUNTRY_NAME, 
            PROVINCE_NAME, STREET_ADDRESS, ACCOUNT_PASSWORD, EMAIL_ADDRESS, ACCOUNT_NAME)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            success = sql.execute_command(cursor, cnx, query, (first_name, last_name, phone_number, country_name, 
                                                          province, street_address, password, email_address, login_name))
            cnx.close()
            if success:
                st.success("Sign Up Seccessfully! Our sales manager will contact you later.")
                st.image('assets/signup_success.jpg')
            else:
                st.warning('Sign up failed!')
