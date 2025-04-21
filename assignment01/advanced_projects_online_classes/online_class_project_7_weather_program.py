# Weather Program Python Project
# In this Code With Tomi tutorial, you will learn how to build a program that 
# collects user data on a specific location and outputs the weather details 
# of that provided location. This is a great project to start learning
#  how to get data from API's.
import requests

def get_weather(latitude, longitude, city):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data["current_weather"]
        temp = weather["temperature"]
        wind_speed = weather["windspeed"]
        
        print(f"\n📍 City: {city}")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"💨 Wind Speed: {wind_speed} km/h")
    else:
        print("❌ Error fetching weather data")

# 📍 City list with Latitude & Longitude
cities = {
    "Karachi": (24.8607, 67.0011),
    "Lahore": (31.5497, 74.3436),
    "Islamabad": (33.6844, 73.0479),
    "New York": (40.7128, -74.0060),
    "London": (51.5074, -0.1278)
}

# 🌍 User se city input lo
city_name = input("Enter city name: ").title()

if city_name in cities:
    lat, lon = cities[city_name]
    get_weather(lat, lon, city_name)
else:
    print("❌ City not found! Try another city.")
