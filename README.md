# 🌦 Weather ETL Pipeline

A simple Python ETL pipeline that fetches real-time weather data from the OpenWeather API every 5 minutes and saves it to a CSV file.
## ⚙️ Tech Stack
- Python 3
- requests
- pandas
- schedule

## 🧠 Features
- Extracts live weather data using OpenWeather API
- Transforms JSON into structured data
- Loads incremental data into CSV
- Runs automatically every 5 minutes

## 🚀 Setup

1. Clone this repository:
   ```bash
   git clone  https://github.com/sshossen/weather_ctg.git
   cd weather-api-etl
2. Create virtual environment and install dependencies:
	```bash
	`python -m venv venv
	venv\Scripts\activate
	pip install -r requirements.txt`
	
3. Edit these lines in `weather_etl.py`:
	```bash
	api_key = 'b38e08962eb2cd65e5644744af042b9a'
	city_name = 'Chittagong'
		
5. Run the script:
	```bash
	python weather_etl.py