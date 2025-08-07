# Weather API Setup Guide

## Quick Setup

### 1. Get a Free API Key

1. Go to https://openweathermap.org/
2. Click "Sign Up" and create a free account
3. After signing up, go to your profile and find your API key
4. Copy the API key (it looks like: `1234567890abcdef1234567890abcdef`)

### 2. Add to Environment

Add this line to your `.env` file:

```env
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual API key.

### 3. Install Dependencies

```bash
uv sync
```

That's it! You're ready to use the weather tools.

## Available Tools

### `get_current_weather`
Get current weather for any city:

```
get_current_weather("London")
get_current_weather("New York", "US")
get_current_weather("Tokyo", "JP")
```

## Example Output

```
🌤️  WEATHER FOR London, GB
========================================
🌡️  Temperature: 18°C
🤔 Feels like: 16°C
💧 Humidity: 65%
💨 Wind Speed: 3.2 m/s
☁️  Conditions: Partly Cloudy
```

## Free Tier Limits

- 1,000 API calls per day
- Current weather and 5-day forecast
- Perfect for personal use!

## Troubleshooting

- **"City not found"**: Check spelling or add country code
- **"API key not found"**: Make sure you added it to `.env`
- **Rate limit errors**: Wait a few minutes and try again 