# Imports
from signUpBackend import *
from signIn import check_password, authenticate_user
from landingPageBackend import HEADING, SUB_HEADING
from signUpBackend import *
import os
import json


# Given Details
first_name = "Tejas"
last_name = "Raghuram"
street_name = "Fox Hill Run"
street_number = "16"
password = "password"
confirm_password = "password"
state = "NJ"
city = "Basking"
zip_code = "08876"
phone_number = "7328237778"
email = "tejas.raghuram@rutgers.edu"

# Create a new user and complete all necessary steps
result = create_complete_new_user(last_name=last_name, first_name=first_name, street_name=street_name, 
                                  street_number=street_number, state=state, city=city, zip_code=zip_code,
                                  phone_number=phone_number, email=email, password=password, 
                                  confirm_password=confirm_password)

# Print the result
if result["status"] == "Success":
    print("User created successfully!")
else:
    print(result["message"])