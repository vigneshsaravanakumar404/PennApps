# Imports
import os
import json
import bcrypt  # Import the bcrypt library

# Backend Variables
FILE_NAME = "users.json"

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

def save_user(user, password, passwordConfirmation):
    """Save a user to the file."""
    # Check if passwords match
    if password != passwordConfirmation:
        return "Error: Password and confirmation password do not match"
    
    # Check if user already exists
    if user_exists(user['phone_number'], user['email']):
        return "Error: The user already exists"
    
    users = []
    
    # If the file already exists, load the current users
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            users = json.load(file)
    
    # Append the new user
    users.append(user)
    
    # Save the updated users list back to the file
    with open(FILE_NAME, 'w') as file:
        json.dump(users, file)
    return "User saved successfully"

def get_users():
    """Retrieve all users from the file."""
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []




# Example Code
first_name = "Vignesh"
last_name = "Saravanakumar"
edu_email = "vignesh.saravanakumar@rutgers.edu"
college = "Rutgers University"
password = "secure_password"
passwordConfirmation = "secure_password"
phoneNumber = "8482789466"

# Check if passwords match and hash the password
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
    "college": password
}

# Save the user and print the result
print(save_user(new_user, password, passwordConfirmation))