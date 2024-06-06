import json
import os
from getpass import getpass

USERS_FILE = 'users.json'

class User:
    # Constructor for User class
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def load_users():
        # Check if user file exists and load users
        if not os.path.exists(USERS_FILE):
            return {}
        with open(USERS_FILE, 'r') as file:
            return json.load(file)

    @staticmethod
    def create_user(username, password):
        # Create a new user and save it to the users file
        users = User.load_users()
        if username in users:
            print(f"Username already exists: {username}")
            return False
        # Create a new user with the given username and password
        users[username] = {'password': password}
        # Save the users to the users file 
        User.save_users(users)
        return True

    @staticmethod
    def save_users(users):
        with open(USERS_FILE, 'w') as file:
            json.dump(users, file)

    @staticmethod
    def authenticate_user(username, password):
        # Authenticate the user with the given username and password
        users = User.load_users()
        if username not in users:
            return False
        if users[username]['password'] != password:
            return False
        return True
