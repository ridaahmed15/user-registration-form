import streamlit as st
from utils import validate_login  #ek likha kiu k compara krwana h bs validation hgain sari

st.set_page_config(
    page_title="User Login",
    layout="centered"
)

st.title("User Login")
st.markdown("Welcome Back!Please Login To Continue")

if 'logged-in' not in st.session_state:
    st.session_state.logged_in=False
if 'current_user' not in st.session_state:
    st.session_state.current_user=None

#login Form

with st.form("login_form"):
    user_id=st.text_input(
        "User ID",
        placeholder="Enter your User ID",
        help="Enter your User ID you register with"
    )

    password=st.text_input(
        "password",
        type="password",
        placeholder="Enter your password",
        help="Enter your password"
    
    )

    submitted=st.form_submit_button("Login",use_container_width=True)

    #process login

    if submitted:
        if not user_id or not password:
            st.error("Please fill in both fields!")

        else:
            success,message = validate_login(user_id,password)

            if success:
                st.session_state.logged_in=True
                st.session_state.current_user=user_id
                st.success(f"{message}")
            else:
                st.error(f"{message}")
