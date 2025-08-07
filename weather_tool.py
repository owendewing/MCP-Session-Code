import requests
import os
from typing import Dict, Any

def get_weather(city: str, country_code: str = "") -> str:
    """
    Get current weather information for a city
    
    Args:
        city: City name (e.g., "London", "New York")
        country_code: Optional country code (e.g., "US", "GB")
    """
    try:
        # Get API key from environment
        api_key = os.getenv("OPENWEATHER_API_KEY")
        if not api_key:
            return "Error: OPENWEATHER_API_KEY not found in environment variables. Please add it to your .env file."
        
        # Build location string
        location = city
        if country_code:
            location = f"{city},{country_code}"
        
        # Make API request
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location,
            "appid": api_key,
            "units": "metric"  # Use Celsius
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract weather information
            weather_desc = data["weather"][0]["description"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            city_name = data["name"]
            country = data["sys"]["country"]
            
            # Format the response
            weather_report = [
                f"🌤️  WEATHER FOR {city_name}, {country}",
                "=" * 40,
                f"🌡️  Temperature: {temp}°C",
                f"🤔 Feels like: {feels_like}°C",
                f"💧 Humidity: {humidity}%",
                f"💨 Wind Speed: {wind_speed} m/s",
                f"☁️  Conditions: {weather_desc.title()}"
            ]
            
            return "\n".join(weather_report)
            
        elif response.status_code == 404:
            return f"Error: City '{city}' not found. Please check the spelling or try a different city."
        else:
            return f"Error: API request failed with status code {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to weather service: {str(e)}"
    except Exception as e:
        return f"Error: {str(e)}"
