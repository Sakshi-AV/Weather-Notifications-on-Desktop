import time
import requests
from plyer import notification

# Constants
API_KEY = "f3c44a944bd0e13a8acb5cb9c7b3c2cd"  # Replace with your OpenWeatherMap API Key
CITY_NAME = input("Enter City Name")  # Replace with your city name
URL =f"http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"

def get_weather_info():
    try:
        response = requests.get(URL)
        data = response.json()
        
        if data["cod"] == 200:
            main_data = data.get("main", {})
            temperature = main_data.get("temp")
            pressure = main_data.get("pressure")
            humidity = main_data.get("humidity")
            weather_data = data.get("weather", [])
            if weather_data:
                weather_description = weather_data[0].get("description")
            
            if temperature is not None and pressure is not None and humidity is not None and weather_description:
                # Convert temperature from Kelvin to Celsius
                temperature_celsius = temperature - 273.15
                return f"Temperature: {temperature_celsius:.2f}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_description.capitalize()}"
            else:
                return "Error: Incomplete data in response"
        else:
            return "Error: City Not Found"
    except Exception as e:
        return f"Error: {e}"

def notify_weather():
    weather_info = get_weather_info()
    notification.notify(
        title=f"Weather in {CITY_NAME.capitalize()}",
        message=weather_info,
        timeout=30  # Extend notification timeout to 30 seconds
    )

if __name__== "__main__":
    while True:
        notify_weather()
        time.sleep(3600)  # Notify every 1 hour