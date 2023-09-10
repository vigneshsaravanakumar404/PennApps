# Imports
from signUpBackend import *
from signIn import check_password, authenticate_user
from signUpBackend import *
import os
import json

# Given Details
first_name = "Esha"
last_name = "VigneswaranSS"
street_name = "Her Mom's House"
street_number = "0"
password = "bad"
confirm_password = "bad"
state = "NJ"
city = "Dayton"
zip_code = "08810"
phone_number = "2313-456-7802"
email = "eshaSSSSSSSSSSSs.vigneswaran@mit.edu"
IDS = []

# Create a new user and complete all necessary steps
result = create_complete_new_user(last_name=last_name, first_name=first_name, street_name=street_name, 
                                  street_number=street_number, state=state, city=city, zip_code=zip_code,
                                  phone_number=phone_number, email=email, password=password, 
                                  confirm_password=confirm_password)

# get the customer id of the new user
customer_id_example = CUSTOMER_ID



# Example usage:
result = create_accounts_for_customer123("64fd0b3e9683f20dd51880cc")
print(result)
