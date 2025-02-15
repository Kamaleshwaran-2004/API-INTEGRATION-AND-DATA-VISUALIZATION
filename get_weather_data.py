import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

API_KEY = "345023f67b1555d1d3f0e8b5df7510f6"
CITY = "London"
UNITS = "metric" 

def fetch_weather_data(city, api_key, units="metric"):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={ "345023f67b1555d1d3f0e8b5df7510f6"}&unit=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

def process_weather_data(data):
    timestamps = []
    temperatures = []
    humidity = []

    for entry in data['list']:
        dt = datetime.datetime.fromtimestamp(entry['dt'])
        timestamps.append(dt)
        temperatures.append(entry['main']['temp'])
        humidity.append(entry['main']['humidity'])

    return timestamps, temperatures, humidity

def visualize_weather(timestamps, temperatures, humidity):
    sns.set_style("darkgrid")
    plt.figure(figsize=(12, 6))


    plt.plot(timestamps, temperatures, label="Temperature (°C)", color="red", marker='o')
    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Forecast')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, humidity, label="Humidity (%)", color="blue", marker='o')
    plt.xlabel('Date & Time')
    plt.ylabel('Humidity (%)')
    plt.title('Humidity Forecast')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

def main():
    data = fetch_weather_data(CITY, API_KEY, UNITS)
    if data:
        timestamps, temperatures, humidity = process_weather_data(data)
        visualize_weather(timestamps, temperatures, humidity)

if __name__ == "__main__":
    main()
