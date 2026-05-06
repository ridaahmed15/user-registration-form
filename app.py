import streamlit as st
import pandas as pd
from utils import init_csv

#page configuration

st.set_page_config(
    page_title="User Management System",
    layout="wide",
    initial_sidebar_state="expanded"
)

#initial
init_csv()

#title

st.title("User Managment System")
st.sidebar.title("Navigation")

#creating navigation buttons

if 'page' not in st.session_state:
    st.session_state.page="Login"

col1,col2 =st.columns(2)
if col1.button("Register"):
    st.session_state.page="Register"
if col2.button("Login"):  
    st.session_state.page="Login"
st.sidebar.info("""
- USER ID: 4-20 Characters
- Password: 8-20 Characters with Upercase and lowercase letters
- Email: Valid Format
-Phone: must be pakistani format""")

if st.session_state.page =="Register":
    st.switch_page("pages/01_register.py")
else:
    st.switch_page("pages/02_login.py")