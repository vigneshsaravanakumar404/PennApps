# Imports
from API import API_KEY
import os
import json
import bcrypt  # Import the bcrypt library
import requests

# Backend Variables
FILE_NAME = "users.json"
BASE_URL = "http://api.nessieisreal.com"
create_new_account = None
credit_account = None
debit_account = None

# Backend Functions
def hash_password(password: str) -> bytes:
    """Hash and salt the password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def user_exists(phone_number, email):
    """Check if a user with the given phone number or email already exists."""
    users = get_users()
    for user in users:
        if user['phone_number'] == phone_number or user['email'] == email:
            return True
    return False

def validate_account(api_key, account_id):
    endpoint = f"{BASE_URL}/accounts/{account_id}?key={api_key}"
    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def create_new_account(api_key, customer_id, account_type="Savings", nickname="New Account", balance=0, rewards=0):
    endpoint = f"{BASE_URL}/customers/{customer_id}/accounts?key={api_key}"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "type": account_type,
        "nickname": nickname,
        "rewards": rewards,
        "balance": balance,
    }
    
    response = requests.post(endpoint, headers=headers, json=body)
    if response.status_code == 201:
        return response.json()
    else:
        return None

def create_new_customer(first_name, last_name, street_number, street_name, city, state, zip_code):
    endpoint = f"{BASE_URL}/customers?key={API_KEY}"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "first_name": first_name,
        "last_name": last_name,
        "address": {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip": zip_code
        }
    }
    
    response = requests.post(endpoint, headers=headers, json=body)
    if response.status_code == 201:
        return response.json()
    else:
        return None

def save_user(user, password, passwordConfirmation, account_type="Savings", 
              nickname="New Account", create_new=False, debit_account=None, 
              credit_account=None):
    """Save a user to the file."""
    
    # Check if passwords match
    if password != passwordConfirmation:
        return "Error: Password and confirmation password do not match"
    
    # Check if user already exists
    if user_exists(user['phone_number'], user['email']):
        return "Error: The user already exists. Please Log In"

    # If CREATE_NEW is True, create a new customer first
    if create_new:
        customer_data = create_new_customer(user['first_name'], user['last_name'], 
                                            user['address']['street_number'], user['address']['street_name'], 
                                            user['address']['city'], user['address']['state'], user['address']['zip_code'])
        
        if 'customer_id' in customer_data:
            # Use the customer_id from the created customer to create a new account
            account_data = create_new_account(API_KEY, customer_data['customer_id'], account_type, nickname)
            if 'account_number' in account_data:
                user['user_data']['new_bank_account'] = account_data['account_number']
            else:
                return f"Error creating account: {account_data.get('message', 'Unknown error')}"
        else:
            return f"Error creating customer: {customer_data.get('message', 'Unknown error')}"
    
    # If DEBIT_ACCOUNT or CREDIT_ACCOUNT is provided, validate and add them to user_data
    if debit_account:
        debit_account_data = validate_account(API_KEY, debit_account)
        if debit_account_data:
            user['user_data']['debit_account'] = debit_account_data['account_number']
        else:
            return "Debit account not found or invalid ID"

    if credit_account:
        credit_account_data = validate_account(API_KEY, credit_account)
        if credit_account_data:
            user['user_data']['credit_account'] = credit_account_data['account_number']
        else:
            return "Credit account not found or invalid ID"

    # If no bank account details are provided and none is created, set user_data to "NONE"
    if not user['user_data']:
        user['user_data']['bank_account'] = "NONE"

    users = []
    
    # If the file already exists, load the current users
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            users = json.load(file)
    
    # Append the new user
    users.append(user)
    
    # Save the updated users list back to the file
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file, indent=4)  # Use 4 spaces for indentation
    
    return "User saved successfully"

def get_users():
    """Retrieve all users from the file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            file_content = file.read()
            if not file_content:  # Check if file is empty
                return []
            try:
                return json.loads(file_content)
            except json.JSONDecodeError:
                return []  # Return an empty list if the file contains invalid JSON data
    return []


# Example Code
""" Required Infomration From New User"""
first_name = "Aryan"
last_name = "Kashyap"
edu_email = "aryan.kashyup@rutgers.edu"
college = "Rutgers University"
password = "secure_password"
passwordConfirmation = "secure_password"
street_number = "123"
street_name = "Main St"
city = "SomeCity"
state = "SomeState"
zip_code = "12345"
phoneNumber = "6092163128"

# Bank Account Information

""" 
# If they don't have an account 

create_new_user = True
chosen_account_type = "Checking"  # Some account type
chosen_account_name = "My Personal Checking"  # Some account name


# if they do have an account

create_new_user = False
customer_id = "123456789"  # Some customer ID
debit_account = "123456789"  # Some account ID
credit_account = "123456789"  # Some account ID
checking_account = "123456789"  # Some account ID
"""

# Account Creation Code
if password == passwordConfirmation:
    hashed_password = hash_password(password)
else:
    print("Passwords do not match!")
    exit()

new_user = {
    "first_name": first_name,
    "last_name": last_name,
    "phone_number": phoneNumber,
    "email": edu_email,
    "password": hashed_password.decode('utf-8'),  # Store the hashed password
    "college": college,
    "address": {
        "street_number": street_number,
        "street_name": street_name,
        "city": city,
        "state": state,
        "zip_code": zip_code
    },
    "user_data": {}  # Empty JSON object for user-specific data
}

# Save the user and print the result
print(save_user(new_user, password, passwordConfirmation, chosen_account_type, chosen_account_name))