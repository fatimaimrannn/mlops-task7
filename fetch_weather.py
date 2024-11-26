import requests
import csv
from datetime import datetime

# Replace with your new OpenWeatherMap API key
api_key = "api-key"
city = "London"  # Replace with the desired city
url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&cnt=5&appid={api_key}"

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    
    # Print the entire response to see its structure
    print(data)

    # Ensure the 'list' key exists in the response
    if 'list' in data:
        # Prepare the CSV file for saving data
        fields = ['Date', 'Time', 'Temperature', 'Humidity', 'Wind Speed', 'Weather Condition']
        filename = "raw_data.csv"

        # Open CSV file and write headers
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fields)

            # Process the API data and write rows for each entry
            for entry in data['list']:
                date_time = datetime.utcfromtimestamp(entry['dt'])
                date = date_time.strftime('%Y-%m-%d')
                time = date_time.strftime('%H:%M:%S')
                temperature = entry['main']['temp']
                humidity = entry['main']['humidity']
                wind_speed = entry['wind']['speed']
                weather_condition = entry['weather'][0]['description']

                writer.writerow([date, time, temperature, humidity, wind_speed, weather_condition])

        print(f"Data collected and saved to {filename}")
    else:
        print("Error: 'list' key not found in the API response.")
else:
    print(f"Error: Unable to fetch data from API. Status Code: {response.status_code}")
