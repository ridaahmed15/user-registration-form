#REGISTRATION PAGE

import streamlit as st
#import re #regular expression
from utils import(
    validate_email,validate_name,validate_login,validation_password,validate_phone,validate_user_id,save_user
)

st.set_page_config(
    page_title="UserRegistration",
    layout="centered"
)

st.title("User Registration Form")

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

    with st.form("Registration Form",clear_on_submit=False): #submit krne k bd fieldkoclear krne k method ko clear_on_submit kaheingy
        col1,col2=st.columns(2)

        with col1:
            user_id=st.text_input("User ID *",placeholder="eg:Rafay123",help="4-20 character(letter,numbers,underscores)")   #helpka icon for field info kkia cheez fill honi chhye isfield me
            full_name=st.text_input("Full Name *",placeholder="eg: M Rafay Shaikh",help="2-50 characters {letter, spaces, hyphens}")
            email=st.text_input("Email *",placeholder="eg: rafay@email",help="Must be Valid Email")

        with col2:
            phone=st.text_input("Phone Number *",placeholder="=92300000000",help="Pakistan Format Only!")  #text_input islie use krhy regular expression k method se match krskeintky ,- ajaye
            password=st.text_input("Password *",placeholder="Enter Your Password",help="8-20 chars with uppercase, lowercase, numbers and special characters")
            confirm_password=st.text_input("Confirm Password *",placeholder="Re-Enter Password")

        submitted=st.form_submit_button("Register Now")
