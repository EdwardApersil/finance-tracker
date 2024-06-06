from user import User
from transaction import Transaction
from report import transaction_summary
from getpass import getpass

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == '1':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            if User.create_user(username, password):
                print("User registered successfully!")

        elif choice == '2':
            username = input("Enter username: ")
            password = getpass("Enter password: ")
            if User.authenticate_user(username, password):
                print("Welcome back!, enjoy your stay", username)
                print()
                while True:
                    print("\n1. Add Transaction")
                    print("2. View Transactions")
                    print("3. Generate Summary")
                    print("4. Logout")
                    print()
                    user_choice = input("Choose an option: ")

                    if user_choice == '1':
                        date = input("Enter date (YYYY-MM-DD): ")
                        type = input("Enter transaction type (Income/Expense): ")
                        category = input("Enter category: ")
                        amount = float(input("Enter amount: "))
                        description = input("Enter description: ")
                        Transaction.create_transaction(username, date, type, category, amount, description)
                        print("Transaction added successfully!")
                        print()
                    
                    elif user_choice == '2':
                        transactions = Transaction.view_transactions(username)
                        for transaction in transactions:
                            print(transaction)

                    elif user_choice == '3':
                        transaction_summary(username)

                    elif user_choice == '4':
                        print("Logged out.")
                        print()
                        break
            else:
                print("Invalid credentials!")

        elif choice == '3':
            break

if __name__ == '__main__':
    main()
