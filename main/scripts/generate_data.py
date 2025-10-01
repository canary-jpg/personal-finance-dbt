import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define transaction categories and typical merchants
categories = {
    'Groceries': ['Whole Foods', 'Trader Joes', 'Safeway', 'Target', 'Costco'],
    'Dining': ['Chipotle', 'Starbucks', 'Local Cafe', 'Pizza Place', 'Thai Restaurant', 'Burger Joint'],
    'Transportation': ['Uber', 'Lyft', 'Gas Station', 'Public Transit', 'Parking'],
    'Entertainment': ['Netflix', 'Spotify', 'Movie Theater', 'Concert Venue', 'Gym Membership'],
    'Shopping': ['Amazon', 'Target', 'Clothing Store', 'Home Depot', 'Best Buy'],
    'Utilities': ['Electric Company', 'Internet Provider', 'Water Company', 'Phone Bill'],
    'Healthcare': ['Pharmacy', 'Doctor Visit', 'Dental Office', 'Health Insurance'],
    'Income': ['Paycheck', 'Freelance Payment', 'Refund']
}

# Generate dates for last 6 months
end_date = datetime.now()
start_date = end_date - timedelta(days=180)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

transactions = []

# Generate recurring monthly bills
for month_offset in range(6):
    bill_date = start_date + timedelta(days=30 * month_offset)
    
    # Paycheck (bi-weekly)
    for week in [0, 2]:
        transactions.append({
            'date': bill_date + timedelta(days=week * 7),
            'description': 'Paycheck Direct Deposit',
            'amount': 3500.00,
            'category': 'Income',
            'account_type': 'Checking'
        })
    
    # Monthly bills
    transactions.append({
        'date': bill_date + timedelta(days=1),
        'description': 'Electric Company',
        'amount': -random.uniform(80, 150),
        'category': 'Utilities',
        'account_type': 'Checking'
    })
    
    transactions.append({
        'date': bill_date + timedelta(days=5),
        'description': 'Internet Provider',
        'amount': -79.99,
        'category': 'Utilities',
        'account_type': 'Checking'
    })
    
    transactions.append({
        'date': bill_date + timedelta(days=15),
        'description': 'Netflix',
        'amount': -15.99,
        'category': 'Entertainment',
        'account_type': 'Credit Card'
    })
    
    transactions.append({
        'date': bill_date + timedelta(days=20),
        'description': 'Gym Membership',
        'amount': -45.00,
        'category': 'Entertainment',
        'account_type': 'Credit Card'
    })

# Generate random daily transactions
for date in date_range:
    # Skip some days (not every day has transactions)
    if random.random() < 0.3:
        continue
    
    # 1-4 transactions per day
    num_transactions = random.randint(1, 4)
    
    for _ in range(num_transactions):
        # Exclude Income category for random transactions
        category = random.choice([cat for cat in categories.keys() if cat != 'Income'])
        merchant = random.choice(categories[category])
        
        # Generate realistic amounts based on category
        if category == 'Groceries':
            amount = -random.uniform(20, 150)
        elif category == 'Dining':
            amount = -random.uniform(8, 65)
        elif category == 'Transportation':
            amount = -random.uniform(5, 80)
        elif category == 'Entertainment':
            amount = -random.uniform(10, 100)
        elif category == 'Shopping':
            amount = -random.uniform(15, 300)
        elif category == 'Healthcare':
            amount = -random.uniform(20, 200)
        else:
            amount = -random.uniform(10, 100)
        
        # Randomly assign to checking or credit card
        account_type = random.choice(['Checking', 'Credit Card'])
        
        transactions.append({
            'date': date,
            'description': merchant,
            'amount': round(amount, 2),
            'category': category,
            'account_type': account_type
        })

# Create DataFrame
df = pd.DataFrame(transactions)
df = df.sort_values('date').reset_index(drop=True)

# Add transaction ID
df.insert(0, 'transaction_id', range(1, len(df) + 1))

# Format date
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# Display summary
print(f"Generated {len(df)} transactions from {df['date'].min()} to {df['date'].max()}")
print(f"\nTransaction summary by category:")
print(df.groupby('category')['amount'].agg(['count', 'sum']).round(2))
print(f"\nTotal income: ${df[df['amount'] > 0]['amount'].sum():,.2f}")
print(f"Total expenses: ${abs(df[df['amount'] < 0]['amount'].sum()):,.2f}")

# Save to CSV
df.to_csv('../data/transactions.csv', index=False)
print("\nData saved to 'transactions.csv'")
print("\nFirst few rows:")
print(df.head(10))