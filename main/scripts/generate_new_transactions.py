import pandas as pd 
import random
from datetime import datetime, timedelta

#set random seed
random.seed(123)

#generating transactions from last 3 days
end_date = datetime.now()
start_date = end_date - timedelta(days=3)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

categories = {
    'Groceries': ['Trader Joes', 'Foodtown'],
    'Dining': ['Chipotle', 'Blue Bell Coffee', 'Cafe Lyria'],
    'Transportation': ['Uber', 'Public Transportation'],
    'Shopping': ['Amazon', 'Target']
}

transactions = []
transaction_id_start = 10000

for date in date_range:
    num_transactions = random.randint(2, 5)

    for i in range(num_transactions):
        category = random.choice(list(categories.keys()))
        merchant = random.choice(categories[category])

        if category == 'Groceries':
            amount = -random.uniform(30, 100)
        elif category == 'Dining':
            amount = -random.uniform(10, 40)
        else:
            amount = -random.uniform(15, 80)

    transactions.append({
        'transaction_id': transaction_id_start + len(transactions),
        'date': date.strftime('%Y-%m-%d'),
        'description': merchant,
        'amount': round(amount, 2),
        'category': category,
        'account_type': random.choice(['Checking', 'Credit Card'])
    })

df = pd.DataFrame(transactions)
df.to_csv('../data/new_transactions.csv', index=False)
print(f"Generated {len(df)} new transactions")
print(df.head(10))