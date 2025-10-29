import requests
from datetime import datetime
import pandas as pd
import schedule
import time
api_key = 'b38e08962eb2cd65e5644744af042b9a'
city_name = 'Chittagong'
file_name = 'C:/Users/User/weather_api/weather_data.csv'

def fetch_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        record ={
            'city': data['name'],
            'temp_c': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    df = pd.DataFrame(data=[record])

    df.to_csv(file_name, mode='a', index=False, header= not pd.io.common.file_exists(file_name))
schedule.every(5).minutes.do(fetch_weather)

while True:
    schedule.run_pending()
    time.sleep(2)