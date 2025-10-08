import pandas as pd 
import numpy as np 
from datetime import datetime, timedelta
import random 

#set random seed
np.random.seed(42)
random.seed(42)

#generate dates for last 6 months
end_date = datetime.now()
start_date = end_date - timedelta(days=180)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

#define a small portfolio
stocks = {
    'AAPL': {'initial_price': 170, 'volatility': 2},
    'GOOGL': {'initial_price': 140, 'volatility': 3},
    'MSFT': {'initial_price': 380, 'volatility': 5},
    'TSLA': {'initial_price': 250, 'volatility': 8}
}

stock_data = []

for symbol, info in stocks.items():
    price = info['initial_price']
    shares_owned = random.randint(5, 20)

    for date in date_range:
        price_change = np.random.normal(0, info['volatility'])
        price = max(price + price_change, 1)

        stock_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'symbol': symbol,
            'price': round(price, 2),
            'shares_owned': shares_owned,
            'portfolio_value': round(price * shares_owned, 2)
        })

df = pd.DataFrame(stock_data)
print(f"Generated {len(df)} stock records")
print(f"\nSummary by stock:")
print(df.groupby('symbol')[['price', 'portfolio_value']].agg(['min', 'max', 'mean']).round(2))

df.to_csv('../data/stock_data.csv', index=False)
print("\nData saved to data/stock_data.csv")