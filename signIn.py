# Imports
import bcrypt
import os
import json

# Backend Variables
FILE_NAME = "users.json"

# Backend Functions
def check_password(hashed_password: bytes, user_password: str) -> bool:
    """Verify the password against its hashed version."""
    return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password)

def get_users():
    """Retrieve all users from the file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def authenticate_user(identifier, password):
    """Authenticate a user using either phone number or email."""
    users = get_users()
    for user in users:
        if user['phone_number'] == identifier or user['email'] == identifier:
            # Check if the password matches
            if check_password(user['password'].encode('utf-8'), password):
                return "Login successful!"
            else:
                return "Incorrect password!"
    return "User not found!"

# Example code
identifier = "8482789466" # Email or phone number
password = "secure_password" 

# Authenticate and print the result
print(authenticate_user(identifier, password))