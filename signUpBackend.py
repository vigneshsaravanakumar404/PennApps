# Imports
from API import API_KEY
from capitalOneMethods import *
import os
import json
import bcrypt  # Import the bcrypt library
import requests

# Backend Variables
FILE_NAME = "users.json"
BASE_URL = "http://api.nessieisreal.com"

# Backend Functions
def hash_password(password: str) -> bytes:
    """Hash and salt the password."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def create_new_user(first_name: str, last_name: str, phone_number: str, email: str, password: str, confirm_password: str) -> dict:
    """
    Creates a new user with the provided details.

    Parameters:
    - first_name (str): First name of the user.
    - last_name (str): Last name of the user.
    - phone_number (str): Phone number of the user.
    - email (str): Email address of the user.
    - password (str): Password chosen by the user.
    - confirm_password (str): Password confirmation.
    - has_capital_one_account (bool): Indicates if the user already has a Capital One account.

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
        "password": hashed_password.decode('utf-8'),  # Store the hashed password
    }

    # Save the user to a file or database (this part is skipped for brevity)
    # For example: save_user_to_database(user) 

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
    
    return "User saved successfully."

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

def create_customer_and_accounts(identifier: str) -> dict:
    """
    Creates a new customer in Capital One API and sets up specified accounts for them.

    Parameters:
    - identifier (str): Phone number or email address of the user.

    Returns:
    - dict: A dictionary containing customer and account details or error messages.
    """
    
    # Step 1: Fetch user details from the local database
    user = get_user_from_database(identifier)  # Assuming this function exists and fetches user by phone or email
    
    if not user:
        return {"error": "User not found in the database!"}

    # Step 2: Create the customer using Capital One API
    customer_data = {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "address": user["location"]
    }
    customer_response = create_customer(customer_data)
    
    if 'error' in customer_response:
        return {"error": f"Error creating customer: {customer_response['message']}"}
    
    customer_id = customer_response["_id"]

    # Step 3: Create the four accounts for this customer
    account_types = ["Checking", "Savings", "Debit", "Credit Card"]
    accounts = {}

    for acc_type in account_types:
        account_data = {
            "type": acc_type,
            "nickname": f"{user['first_name']} {user['last_name']}'s {acc_type} Account",
            "balance": 0
        }
        if acc_type == "Credit Card":
            account_data["rewards"] = 0
        account_response = create_account(customer_id, account_data)
        
        if 'error' in account_response:
            return {"error": f"Error creating {acc_type} account: {account_response['message']}"}
        
        accounts[acc_type] = account_response["_id"]

    return {"message": "Accounts successfully created!", "accounts": accounts}

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

def create_account(customer_id: str, account_type: str, nickname: str, rewards: int, balance: float, account_number: str) -> dict:
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
        "account_number": account_number
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()

def create_complete_new_user(last_name: str, first_name: str, street_name: str, street_number: str, state: str, city: str, 
                             zip_code: str, phone_number: str, email: str, has_capital_one_account: bool) -> dict:
    """
    Create a new user from start to finish.

    Parameters:
    - last_name, first_name, street_name, street_number, state, city, zip_code, phone_number, email: User details.
    - has_capital_one_account (bool): Indicates if the user already has a Capital One account.

    Returns:
    - dict: A dictionary containing status, message, and any relevant data.
    """
    
    # Step 1: Check if the user is unique
    is_unique = is_unique_user(phone_number, email)
    if not is_unique:
        return {
            "status": "Failed",
            "message": "User with the provided phone number or email already exists."
        }

    # Step 2: Create a new user
    user = create_new_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, 
                           street_number=street_number, street_name=street_name, city=city, state=state, 
                           zip_code=zip_code, has_capital_one_account=has_capital_one_account)

    # Step 3: Save the user to a file
    save_status = save_user_to_file(user)
    if save_status != "Success":
        return {
            "status": "Failed",
            "message": "Error saving user to the database."
        }

    # Step 4: If the user doesn't have a Capital One account, create one
    if not has_capital_one_account:
        creation_status = create_customer_and_accounts(email or phone_number)
        if creation_status.get("code") != 0:
            return {
                "status": "Failed",
                "message": "Error creating Capital One customer and accounts.",
                "details": creation_status
            }
    
    return {
        "status": "Success",
        "message": "User successfully created and saved.",
        "user": user
    }