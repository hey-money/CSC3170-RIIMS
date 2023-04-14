import streamlit as st
import mysql.connector
import pandas as pd

from utils.control import *


def log_in_page():
    cnx = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="project") 
    
    st.text("Please login here.")
    restaurant_name = st.text_input("Restaurant name", placeholder="Fake login name: a")
    password = st.text_input("Password", placeholder="Fake login password: 1")

    # # Get a cursor
    # cur = cnx.cursor()
    # # Execute a query
    # cur.execute("""
    #             SELECT ROLE, USER_ID  
    #             FROM user
    #             WHERE (FIRST_NAME = %s)
    #             AND (LAST_NAME = %s)
    #             AND (PASSWORD = %s);
    #             """, (first_name,last_name,password))
    # result = cur.fetchone()
    # if result:
    #    ID = result

    # aka. "RestaurantID"
    # Temp login info
    # if restaurant_name in ['a']:
    #     ID = 114514  
    # else:
    #     ID = None
    ID = 114514  


    # Fetch one result
    if st.button("Log In!"):
        if ID == None:
            st.warning("INVALID INFORMATION! RECHECK YOUR INPUT!")
        else:
            move_to_backend_state()
            if "RestaurantID" not in st.session_state: 
                st.session_state["RestaurantID"] = 0
            st.session_state["RestaurantID"] = ID
            st.success("Log in Seccessfully as staff. Please click the button again.")
            st.balloons()

    cnx.close()

def sign_up_page():
    st.text("Please leave your information here, our sales manager will contact you later.")

    # cnx = mysql.connector.connect(
    # host="127.0.0.1",
    # port=3306,
    # user="root",
    # password="123456",
    # database="project") 
    # cur = cnx.cursor()

    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    phone_number = st.text_input("Phone Number")

    # Create a selectbox for countries
    country_name = st.selectbox("Select your country:", ['China', 'International'])
    # Create a selectbox for provinces
    if country_name == "China":
        province_options =  ["Anhui", "Beijing", "Chongqing", "Fujian", "Gansu", "Guangdong", "Guangxi", "Guizhou", "Hainan", "Hebei", "Heilongjiang", "Henan", "Hubei", "Hunan", "Jiangsu", "Jiangxi", "Jilin", "Liaoning", "Inner Mongolia", "Ningxia", "Qinghai", "Shaanxi", "Shandong", "Shanghai", 
                        "Shanxi", "Sichuan", "Tianjin", "Tibet", "Xinjiang", "Yunnan", "Zhejiang", 
                        "Taiwan", "Hong Kong", "Macau"]
        province = st.selectbox("Select a province:", province_options)
    # else:
    #     province = st.selectbox("Select a province:", ["International",])

    street_address = st.text_input("Street Address")

    password = st.text_input("Account password")

    if st.button("Sign Up"):
    # if st.button("Sign Up") and first_name and last_name and phone_number and country_name and street_address and password:
        # query = """
        # INSERT INTO user (FIRST_NAME, LAST_NAME, PHONE_NUMBER, COUNTRY_NAME, PROVINCE, ROLE, STREET_ADDRESS, PASSWORD)
        # VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        # """
        # cur.execute(query, (first_name, last_name, phone_number, country_name, province, role, street_address, password))
        # cnx.commit()
        st.success("Sign Up Seccessfully! Our sales manager will contact you later.")
        st.image('assets/signup_success.jpg')
    # cnx.close()