import requests
import pandas as pd
from datetime import datetime, timedelta
import time

# Configuration
API_KEY = '9991ff91cfd37e8a9bbb02940193ba76' 
CITY = 'New York'  # Your location
LAT = 40.7128
LON = -74.0060

# Free tier allows historical data via current weather API
# For historical, we'll simulate or use One Call API

def get_current_weather():
    """Fetch current weather"""
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=imperial"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'weather_condition': data['weather'][0]['main'],
            'description': data['weather'][0]['description']
        }
    else:
        print(f"Error: {response.status_code}")
        return None

# For now, let's create a simple current weather record
weather = get_current_weather()
if weather:
    df = pd.DataFrame([weather])
    df.to_csv('../data/weather_data.csv', index=False)
    print("Weather data saved!")
    print(df)
else:
    print("Failed to fetch weather data")