#REGISTRATION PAGE

import streamlit as st
#import re #regular expression
from utils import (
    validate_email,validate_name,validate_login,validation_password,
    validation_phone,validate_user_id,save_user
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
        full_name=st.text_input("Full Name *",placeholder="eg: M Rafay Shaikh",help="2-50 characters (letter, spaces, hyphens)")
        email=st.text_input("Email *",placeholder="eg: rafay@email",help="Must be Valid Email")

    with col2:
        phone=st.text_input("Phone Number *",placeholder="=92300000000",help="Pakistan Format Only!")  #text_input islie use krhy regular expression k method se match krskeintky ,- ajaye
        password=st.text_input("Password *",placeholder="Enter Your Password",help="8-20 chars with uppercase, lowercase, numbers and special characters")
        confirm_password=st.text_input("Confirm Password *",placeholder="Re-Enter Password")

    submitted=st.form_submit_button("Register Now",use_container_width=True)


        #validation & Processing -BY USING LIST


    if submitted:
        errors=[]
        warnings=[]
                
        #USER ID VALIDATIONS

        user_id_valid, user_id_msg = validate_user_id(user_id)

        if not user_id_valid:
            errors.append(f"{user_id_msg}")
        elif user_id:
            warnings.append(f"{user_id_msg}")

        #Name Validation

        name_valid,name_msg=validate_name(full_name, "Full Name") #do variablesbna k validate_name kopass krainge
        if not full_name:
            errors.append("Full Name Required")
        elif not name_valid:
            errors.append(f"{name_msg}")
        else:
            warnings.append(f"{name_msg}")

        #EMAIL VALIDATION

        if not email:
            errors.append("Email Address Required")

        else:
            email_valid,email_msg=validate_email(email)
            if not email_valid:
                errors.append(f"{email_msg}")

            else:
                warnings.append(f"{email_msg}")


        #phone validation

        if not phone:
            errors.append("Phone Number Is Required!")
        else:
            phone_valid,phone_msg=validation_phone(phone)
            if not phone_valid:
                errors.append(f"{phone_msg}")
            else:
                warnings.append(f"{phone_msg}")

        #PASSWORD VALIDATION

        if not password:
            errors.append("Password is Required!")
            password_valid,password_msg=validation_password(password)
            if not password_valid:
                errors.append(f"{password_msg}")
            elif password and confirm_password:
                warnings.append(f"{password_msg}")

        #DISPLAYING WARNINGS

        if warnings:
            with st.expander("Validations Passed!",expanded=False):
                for warnings in warnings:
                    st.success(warnings)

        #DISPLAYING ERRORS

        if errors:
            with st.expander("Please Fix The Error",expanded=True):
                for error in errors:
                    st.error(error)

        else:
            #ALL VALIDATIONS PASSED
            if save_user(user_id,full_name,email,phone,password):
                st.success("REGISTRATION SUCCESSFULL!")

   

        


            


                





