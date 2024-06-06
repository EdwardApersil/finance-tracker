import pandas as pd
import matplotlib.pyplot as plt
from transaction import Transaction

def transaction_summary(username):
    transactions = Transaction.load_transactions().get(username, [])
    if not transactions:
        print('No transactions found')
        return
        
    df = pd.DataFrame(transactions)
    df['date'] = pd.to_datetime(df['date'])

    # Convert date column to period(Month) for grouping
    df['month'] = df['date'].dt.to_period('M')

    # Group by month and sum the amounts
    monthly_summary = df.groupby('month')['amount'].sum()
    print(monthly_summary)

    # Plotting
    monthly_summary.plot(kind='bar', title='Monthly Summary')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.show()
