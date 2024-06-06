import json
import os
from datetime import datetime

TRANSACTIONS_FILE = 'transactions.json'

class Transaction:

    # Constructor for Transaction class
    def __init__(self, username, date, type, category, amount, description):
        self.username = username
        self.date = date
        self.type = type
        self.category = category
        self.amount = amount
        self.description = description

    @staticmethod
    def load_transactions():
        # Check if transaction file exists and load transactions
        if not os.path.exists(TRANSACTIONS_FILE):
            return {}
        with open(TRANSACTIONS_FILE, 'r') as file:
            return json.load(file)

    @staticmethod
    def create_transaction(username, date, type, category, amount, description):
        # Create a new transaction and save it to the transactions file
        transactions = Transaction.load_transactions()
        # Generate a unique id for the new transaction
        transaction_id = str(datetime.now())
        # Add the new transaction to the list of transactions for the given user
        if username not in transactions:
            transactions[username] = []
        transactions[username].append({
            'transaction_id': transaction_id,
            'date': date,
            'type': type,
            'category': category,
            'amount': amount,
            'description': description
        })
        Transaction.save_transactions(transactions)

    @staticmethod
    def save_transactions(transactions):
        # Save the updated transactions to the transactions file
        with open(TRANSACTIONS_FILE, 'w') as file:
            json.dump(transactions, file)

    @staticmethod
    def view_transactions(username):
        # Load all the transactions for the given user
        transactions = Transaction.load_transactions()
        return transactions.get(username, [])
