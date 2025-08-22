def get_weather(city):
    # Simple fixed weather data (no API, just demo)
    weather_data = {
        "Ujjain": {"temp": 30, "weather": "sunny", "humidity": 70},
        "Delhi": {"temp": 35, "weather": "hot", "humidity": 50},
        "London": {"temp": 18, "weather": "cloudy", "humidity": 80}
    }

    if city in weather_data:
        data = weather_data[city]
        print("City:", city)
        print("Temperature:", data["temp"], "°C")
        print("Weather:", data["weather"])
        print("Humidity:", data["humidity"], "%")
    else:
        print("Weather data not available for", city)

# Example usage
city_name = input("Enter city name: ")
get_weather(city_name)