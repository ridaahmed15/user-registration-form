import pandas as pd
import os
import re #regular expression
from datetime import datetime

CSV_FILE = "user_data.csv"

#inititalizing csv file with columns

def init_csv():
    if not os.path.exists(CSV_FILE):
        df = pd.DataFrame(columns=[
            'user_id','full name','email','phone','password','registration_date','last_login'
        ])
        df.to_csv(CSV_FILE, index=False)


#validation funcation


def validate_email(email):
    """Email Validation Using Regex"""
    pattern= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0_9._]+\.[a-zA-Z]{2,}$'
    if re.match(pattern,email):
        return True, "Valid Email"
    return False, "Invalid Email Format i.e user@domain.com"


def validate_phone(phone):
    """Phone Validation for Pakistani number format"""
    #Removing spaces and dashes from phone number

    phone = re.sub(r'[\s\-]','',phone)

#check different phone formats


def validation_phone(phone):
    pattern = [
        r'^03[0-9]{9}$',  #03XXXXXXXXXXXXX (Pakistan Mobile Number)
        r'^3[0-9]{9}$',    #3XXXXXXXXXX
        r'^\+923[0-9]{9}$',  #+923XXXXXXXX  
        r'^[0-9]{11}$',     #11 digits 
        r'^00923[0-9]{9}$'
    ]

    for pattern in pattern:
        if re.match(pattern,phone):
            return True, "Valid Phone Number"
    return False, "Invalid Phone Number"
    

def validation_password(password):
    """Password Strenght Validation""" 

    errors=[]

    if len(password) <8:
        errors.append("at least 8 Characters")
    if len(password) >20:
        errors.append("less then 20 Characters")
    if not re.search(r'[A-Z]',password):
        errors.append("at least one uppercase letters")
    if not re.serach(r'[a-z]',password):
        errors.append("at least one lowercase letters")
    if not re.serach(r'[0-9]',password):
        errors.append("at least one number")
    if not re.serach(r'[!@#$%*&^]',password):
        errors.append("At one special character (!@#$%*&^):")  

    if errors:
        return False, f"password must have:{','.join(errors)}"
    return True, "Strong Password"    

def validate_name(name,field_name="Name"):

    if len(name) < 2:
        return False, f"{field_name} must be at least 2 Characters"
    if len(name) >50:
        return False, f"{field_name} must be at least 50 Characters"
    if not re.match(r'^[a-zA-Z\s\-]+$',name):
        return False, f"{field_name} can only contains letters, spaces, and hyphens"
    return True, f"Valid {field_name}"


def validate_user_id(user_id):
    if len(user_id) < 4:
        return False, "User id must be at least of 4 Characters"
    if len(user_id) >20:
        return False, "User id must be at less than 20 Characters"
    if not re.match(r'^[a-zA-Z0-9_]+$',user_id):
        return False, "User ID can only contains letter, characters, numbers and special characters"

#check if user_id already exists
    if os.path.exists(CSV_FILE):
        df=pd.read_csv(CSV_FILE)
        if user_id in df["user_id"].values:
            return False, "USER ID ALREADY EXISTS"
    return True, "Valid User id"


#saving user

def save_user(user_id,full_name,email,phone,password):
        init_csv()

        new_user = pd.DataFrame([{
            'user_id':user_id,
            'full_name':full_name,
            'email':email,
            'phone':phone,
            'password':password,
            'registration_date':datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'last_login':''


        }])


        existing_data=pd.read_csv(CSV_FILE)
        update_data=pd.concat([existing_data,new_user], ignore_index=True)
        update_data.to_csv(CSV_FILE, index=False)
        return True





def validate_login(user_id,password):
    """Check if credentials are correct"""

    init_csv()
    df=pd.read_csv(CSV_FILE)

    #check if user exists
    user_data=df[df['user_id']==user_id]

    if len(user_data)==0:
        return False, "User ID NOT Found!"
    
    #checking password as well

    Stored_password=user_data.iloc[0]['password']

    if Stored_password==password: 
        #updating last login timings
        df.loc[df['user_id']==user_id,'last_login']==datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        df.to_csv(CSV_FILE, index=False)
        return True, f"Welcome Back, {user_data.iloc[0]['full_name']}!"
    return False, "Incorrect Password"


#get user details

def get_user_details(user_id):
    "Get full details by user id"
    df=pd.read_csv(CSV_FILE)
    user_data=df[df['user_id']==user_id]
    if len(user_data)>0:
        return user_data.iloc[0].to_dict()
    return None