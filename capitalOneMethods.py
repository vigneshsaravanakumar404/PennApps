# Imports
from API import API_KEY
import os
import json
import requests

# Backend Variables
BASE_URL = "http://api.nessieisreal.com"

# Backend Functions
def get_customer_accounts(customer_id: str) -> list:
    """
    Fetches the accounts associated with the provided customer ID.
    
    Parameters:
    - customer_id (str): The ID of the customer to fetch accounts for.
    
    Returns:
    - list: A list of accounts associated with the provided customer ID.
    """
    
    endpoint = f"{BASE_URL}/customers/{customer_id}/accounts?key={API_KEY}"
    
    response = requests.get(endpoint)
    
    # If the request was successful, return the list of accounts
    if response.status_code == 200:
        return response.json()
    # If the customer ID does not exist or any other error, return an empty list
    else:
        return []

def create_account_for_customer(customer_id: str, account_type: str, nickname: str, 
                                rewards: int = 0, balance: int = 0) -> dict:
    """
    Creates an account for the customer with the provided ID.
    
    Parameters:
    - customer_id (str): The ID of the customer the account will belong to.
    - account_type (str): The type of account (e.g., "Credit Card").
    - nickname (str): The nickname for the account.
    - rewards (int, optional): The rewards for the account. Defaults to 0.
    - balance (int, optional): The initial balance for the account. Defaults to 0.
    - account_number (str, optional): The account number. If not provided, the bank will generate one.
    
    Returns:
    - dict: A dictionary containing the response code, message, and fields (if any).
    """
    
    endpoint = f"{BASE_URL}/customers/{customer_id}/accounts?key={API_KEY}"
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
    
    # Return the response as a dictionary
    return response.json()

# Example usage:
# response = create_account_for_customer("64fcaeb69683f20dd518803a", "Credit Card", "My Credit Card")
# print(response)

def create_bill_for_account(account_id: str, status: str, payee: str, 
                            nickname: str, payment_date: str, recurring_date: int) -> dict:
    """
    Creates a bill for the account with the provided ID.
    
    Parameters:
    - account_id (str): The ID of the account the bill will belong to.
    - status (str): The status of the bill (e.g., "pending").
    - payee (str): The payee of the bill.
    - nickname (str): The nickname for the bill.
    - payment_date (str): The date the bill will be paid.
    - recurring_date (int): The recurring date for the bill.
    
    Returns:
    - dict: A dictionary containing the response code, message, and fields (if any).
    """
    
    endpoint = f"{BASE_URL}/accounts/{account_id}/bills?key={API_KEY}"
    headers = {
        "Content-Type": "application/json",
    }
    body = {
        "status": status,
        "payee": payee,
        "nickname": nickname,
        "payment_date": payment_date,
        "recurring_date": recurring_date
    }
    
    response = requests.post(endpoint, headers=headers, json=body)
    
    # Return the response as a dictionary
    return response.json()

# Example usage:
# response = create_bill_for_account("some_account_id", "pending", "Utility Company", "Monthly Utility Bill", "2023-09-09", 1)
# print(response)

def get_bills_for_customer(customer_id: str) -> list:
    """
    Retrieves the bills associated with the provided customer ID.
    
    Parameters:
    - customer_id (str): The ID of the customer to fetch bills for.
    
    Returns:
    - list: A list of dictionaries, each representing a bill associated with the customer.
    """
    
    endpoint = f"{BASE_URL}/customers/{customer_id}/bills?key={API_KEY}"
    response = requests.get(endpoint)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        # Return the error message if the request was not successful
        return [response.json()]

# Example usage:
# bills = get_bills_for_customer("some_customer_id")
# for bill in bills:
#     print(bill)

def create_customer(first_name: str, last_name: str, street_number: str, street_name: str, city: str, state: str, zip_code: str) -> dict:
    """
    Creates a new customer.
    
    Parameters:
    - first_name (str): The first name of the customer.
    - last_name (str): The last name of the customer.
    - street_number (str): The street number of the customer's address.
    - street_name (str): The street name of the customer's address.
    - city (str): The city of the customer's address.
    - state (str): The state of the customer's address.
    - zip_code (str): The zip code of the customer's address.
    
    Returns:
    - dict: A dictionary containing the response from the API, which includes the status and any relevant messages.
    """
    
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
    
    # Return the response from the API
    return response.json()

# Example usage:
# response = create_customer("John", "Doe", "123", "Main St", "SomeCity", "SomeState", "12345")
# print(response)

# 1. Fetch Deposits Associated with an Account
def get_deposits(account_id: str) -> list:
    endpoint = f"{BASE_URL}/accounts/{account_id}/deposits?key={API_KEY}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()  # This will return the error message if there's one.

# 2. Create a Deposit for an Account
def create_deposit(account_id: str, medium: str, transaction_date: str, status: str, description: str) -> dict:
    endpoint = f"{BASE_URL}/accounts/{account_id}/deposits?key={API_KEY}"
    body = {
        "medium": medium,
        "transaction_date": transaction_date,
        "status": status,
        "description": description
    }
    response = requests.post(endpoint, json=body)
    return response.json()

# 3. Create a Loan for an Account
def create_loan(account_id: str, loan_type: str, status: str, credit_score: int, monthly_payment: float, amount: float, description: str) -> dict:
    endpoint = f"{BASE_URL}/accounts/{account_id}/loans?key={API_KEY}"
    body = {
        "type": loan_type,
        "status": status,
        "credit_score": credit_score,
        "monthly_payment": monthly_payment,
        "amount": amount,
        "description": description
    }
    response = requests.post(endpoint, json=body)
    return response.json()

# 4. Fetch a Loan by ID
def get_loan(loan_id: str) -> dict:
    endpoint = f"{BASE_URL}/loans/{loan_id}?key={API_KEY}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return response.json()  # This will return the error message if there's one.

def create_withdrawal(account_id: str, medium: str, transaction_date: str, status: str, amount: float, description: str) -> dict:
    endpoint = f"{BASE_URL}/accounts/{account_id}/withdrawals?key={API_KEY}"
    body = {
        "medium": medium,
        "transaction_date": transaction_date,
        "status": status,
        "amount": amount,
        "description": description
    }
    response = requests.post(endpoint, json=body)
    return response.json()