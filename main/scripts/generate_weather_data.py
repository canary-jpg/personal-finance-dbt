import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

#setting random seed
np.random.seed(42)
random.seed(42)

end_date = datetime.now()
start_date = end_date - timedelta(days=180)
date_range = pd.date_range(start=start_date, end=end_date, freq='D')

weather_conditions = ['Clear', 'Clouds', 'Rain', 'Snow', 'Drizzle']
descriptions = {
    'Clear': ['clear sky', 'few clouds'],
    'Clouds': ['scattered clouds', 'broken clouds', 'overcast clouds'],
    'Rain': ['light rain', 'moderate rain', 'heavy rain'],
    'Snow': ['light snow', 'snow'],
    'Drizzle': ['light drizzle']
}

weather_data = []

for date in date_range:
    month = date.month
    if month in [12, 1, 2]:
        base_temp = random.uniform(25, 45)
    elif month in [3, 4, 5]:
        base_temp = random.uniform(45, 65)
    elif month in [6, 7, 8]:
        base_temp = random.uniform(70, 90)
    else:
        base_temp = random.uniform(50, 70)

    condition = random.choice(weather_conditions)

    weather_data.append({
        'date': date.strftime('%Y-%m-%d'),
        'temp': round(base_temp + random.uniform(-5, 5), 1),
        'feels_like': round(base_temp + random.uniform(-8, 3), 1),
        'humidity': random.randint(40, 90),
        'weather_condition': condition,
        'description': random.choice(descriptions[condition])
    })

df = pd.DataFrame(weather_data)

print(f"Generated {len(df)} weather records")
print(f"\nWeather condition distribution:")
print(df['weather_condition'].value_counts())
print(f"\nTemperate stats:")
print(df['temp'].describe())

df.to_csv('../data/weather_data.csv', index=False)
print("\nData saved to data/weather_data.csv")
