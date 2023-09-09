# Imports
from API import API_KEY
from capitalOneMethods import *
import os
import json
import bcrypt  # Import the bcrypt library
import requests
from twilio.rest import Client

# Backend Variables
FILE_NAME = "users.json"
BASE_URL = "http://api.nessieisreal.com"

# Backend Functions
def hash_password(password: str) -> bytes:
    """Hash and salt the password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def create_new_user(first_name, last_name, street_name, street_number, state, city, 
                    phone_number, email, password, confirm_password, zip_code):
    """
    Creates a new user with the provided details.

    Parameters:
    ... (rest of your parameter descriptions)

    Returns:
    - dict: A dictionary containing user details or an error message.
    """
    
    # Check if passwords match
    if password != confirm_password:
        return {"error": "Passwords do not match!"}

    # Hash the password
    hashed_password = hash_password(password)

    # Create the user dictionary
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "phone_number": phone_number,
        "email": email,
        "password": hashed_password.decode('utf-8'),
        "location": {
            "street_number": street_number,
            "street_name": street_name,
            "city": city,
            "state": state,
            "zip_code": zip_code

        }
    }

    return user


def save_user_to_file(user: dict, file_name=FILE_NAME):
    """
    Save a user to the specified file.

    Parameters:
    - user (dict): Dictionary containing user details.
    - file_name (str, optional): Name of the file to save the user to. Defaults to FILE_NAME.

    Returns:
    - str: A message indicating success or failure.
    """
    
    users = []
    
    # Check if the file already exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                return "Error: The file contains invalid JSON data."
    
    # Check if user already exists in the file (based on email, for example)
    for existing_user in users:
        if existing_user['email'] == user['email']:
            return "Error: A user with this email already exists."
    
    # Add the new user to the list
    users.append(user)
    
    # Save the updated user list back to the file
    with open(file_name, 'w') as file:
        json.dump(users, file, indent=4)  # Use 4 spaces for indentation
    
    return "Success"

def is_unique_user(phone_number: str, email: str, file_name=FILE_NAME) -> bool:
    """
    Check if a user with the given phone number or email already exists in the database.

    Parameters:
    - phone_number (str): User's phone number.
    - email (str): User's email.
    - file_name (str, optional): Name of the file to check. Defaults to FILE_NAME.

    Returns:
    - bool: True if the user is unique (doesn't exist in the database), False otherwise.
    """
    
    # Check if the file exists
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                users = json.load(file)
            except json.JSONDecodeError:
                return True  # If file contains invalid JSON, assume user is unique for now
    
    else:
        return True  # If file doesn't exist, user is obviously unique

    # Check each user in the database
    for user in users:
        if user['phone_number'] == phone_number or user['email'] == email:
            return False  # User is not unique

    return True  # User is unique

def create_customer_and_accounts(identifier: str):
    # Assuming you have a function to get user details by email or phone_number
    user = get_user_from_database(identifier)
    
    # Extract necessary details from the user object
    first_name = user['first_name']
    last_name = user['last_name']
    street_number = user['location']['street_number']
    street_name = user['location']['street_name']
    city = user['location']['city']
    state = user['location']['state']
    zip_code = user['location']['zip_code']

    # Create the customer using the Capital One API
    customer_response = create_customer(first_name, last_name, street_number, street_name, city, state, zip_code)

    
    # Check if customer creation was successful
    if "code" in customer_response and customer_response["code"] != 0:
        return customer_response
    
    customer_id = customer_response["customer_id"]
    
    # Create the accounts for the customer
    checking_id = create_account(customer_id, "Checking", "My Personal Checking")
    savings_id = create_account(customer_id, "Savings", "My Personal Savings")
    debit_id = create_account(customer_id, "Debit", "My Debit Card")
    credit_id = create_account(customer_id, "Credit Card", "My Credit Card")
    
    return {
        "code": 0,
        "customer_id": customer_id,
        "checking_id": checking_id,
        "savings_id": savings_id,
        "debit_id": debit_id,
        "credit_id": credit_id
    }

def get_user_from_database(identifier: str) -> dict:
    """
    Fetches user details from the local database (JSON file) based on the provided phone number or email address.

    Parameters:
    - identifier (str): Phone number or email address of the user.

    Returns:
    - dict: A dictionary containing user details or None if the user is not found.
    """
    
    # Check if the file exists
    if not os.path.exists(FILE_NAME):
        return None
    
    # Read from the file
    with open(FILE_NAME, 'r') as f:
        users = json.load(f)
    
    # Search for the user by phone number or email
    for user in users:
        if user["phone_number"] == identifier or user["email"] == identifier:
            return user
    
    return None

def create_account(customer_id: str, account_type: str, nickname: str, rewards: int, balance: float) -> dict:
    """
    Creates a new account for a specified customer.

    Parameters:
    - customer_id (str): The ID of the customer for whom the account is being created.
    - account_type (str): Type of account (e.g., "Credit Card", "Checking").
    - nickname (str): A nickname for the account.
    - rewards (int): Rewards points (applicable for certain account types).
    - balance (float): Initial balance for the account.
    - account_number (str): The account number for the new account.

    Returns:
    - dict: The response from the Capital One API.
    """
    
    url = f"{BASE_URL}/customers/{customer_id}/accounts"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "type": account_type,
        "nickname": nickname,
        "rewards": rewards,
        "balance": balance,
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

    return response.json()
def create_account_for_customer(customer_id: str, account_type: str, nickname: str, rewards: int, balance: int) -> dict:
    """
    Creates an account for the provided customer ID with the specified account type.

    Parameters:
    - customer_id (str): The ID of the customer for whom the account will be created.
    - account_type (str): Type of the account (e.g., "Checking", "Savings", "Credit Card", "Debit Card").
    - nickname (str): Nickname for the account.
    - rewards (int): Rewards associated with the account (usually relevant for Credit Card).
    - balance (int): Initial balance for the account.

    Returns:
    - dict: A dictionary containing the response data from the API.
    """
    
    endpoint = f"{BASE_URL}/customers/{customer_id}/accounts?key={API_KEY}"
    
    account_data = {
        "type": account_type,
        "nickname": nickname,
        "rewards": rewards,
        "balance": balance
    }
    
    response = requests.post(endpoint, json=account_data)
    
    return response.json()

def create_complete_new_user(last_name: str, first_name: str, street_name: str, street_number: str, state: str, 
                             city: str, zip_code: str, phone_number: str, email: str,
                             password: str, confirm_password: str) -> dict:
    """
    Create a new user from start to finish.
    """
    
    # Step 1: Check if the user is unique
    is_unique = is_unique_user(phone_number, email)
    if not is_unique:
        return {
            "status": "Failed",
            "message": "User with the provided phone number or email already exists."
        }

    # Step 2: Create a new user
    user = create_new_user(first_name, last_name, street_name, street_number, state, city, 
                       phone_number, email, password, confirm_password, zip_code)

    # Step 3: Save the user to a file
    save_status = save_user_to_file(user)
    if save_status != "Success":
        return {
            "status": "Failed",
            "message": "Error saving user to the database."
        }

    # Step 4: Create a Capital One customer and accounts
    creation_status = create_customer_and_accounts(email or phone_number)
    if creation_status.get("code") != 201:
        return {
            "status": "Failed",
            "message": "Error creating Capital One customer and accounts.",
            "details": creation_status
        }
    
    # Create the accounts
    customer_id = creation_status["objectCreated"]["_id"]
    checking_id = create_account_for_customer(customer_id, "Checking", "Tejas Checking", 0, 1000)
    savings_id = create_account_for_customer(customer_id, "Savings", "Tejas Savings", 0, 2000)
    debit_id = create_account_for_customer(customer_id, "Debit Card", "Tejas Debit", 0, 500)
    credit_id = create_account_for_customer(customer_id, "Credit Card", "Tejas Credit", 0, 1000)

    # Update the user dictionary with the customer and account IDs
    user["capital_one_data"] = {
        "customer_id": customer_id,
        "checking_id": checking_id,
        "savings_id": savings_id,
        "debit_id": debit_id,
        "credit_id": credit_id
    }

    # Update the user in the file with the new bank details
    save_user_to_file(user)

    # Step 5: Send verification text
    send_verification_text(phone_number)

    return {
        "status": "Success",
        "message": "User successfully created and saved.",
        "user": user
    }

# TODO: IMPLEMENT DYNAMICS
def send_verification_text(phone_number):
    account_sid = "AC250bc634889c756ad404a6274445ed5d"
    auth_token = "15b38101ae6242e8601e5217c5a7dec1"
    verify_sid = "VA2b9577d284546e10bafd9e3c94181018"
    verified_number = "+18482789466"

    client = Client(account_sid, auth_token)

    verification = client.verify.v2.services(verify_sid) \
    .verifications \
    .create(to=verified_number, channel="sms")
    print(verification.status)

    #The code after this is verifying the input
    otp_code = input("Please enter the OTP:")

    try:
        verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=otp_code)
        print(0/0)
        # WILL PRINT APPROVED IF VERIFIED SENT SUCCESSFULLY. WILL THROW ERROR IF WRONG CODE ENTERED perhaps try catch or some shit
    except:
        print("Phone Number Verified")
    
    
