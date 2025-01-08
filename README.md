# Weather App using OpenWeatherMap API

This is a simple weather application built using Python and Tkinter. The app allows users to get current weather information for any city they choose or based on their current location. The app uses the OpenWeatherMap API to fetch weather data and displays it in a user-friendly GUI.

## Features
- Search weather for any city by entering the city name.
- Option to fetch the weather based on the user's current location.
- Displays the current temperature, humidity, pressure, wind speed, and weather description.
- Shows the weather icon corresponding to the current weather.

## Requirements
- Python 3.x
- `tkinter` (for GUI)
- `requests` (for making HTTP requests)
- `geopy` (for geolocation)
- `PIL` (Pillow for image handling)

You can install the necessary packages using pip:

```bash
pip install requests geopy pillow

Setup and Usage
Replace the API_KEY variable in the code with your own API key from OpenWeatherMap.
Run the Python script (weather_app.py).
Enter a city name or use the "Use Current Location" button to get weather details for your location.
View weather data displayed in the app, including temperature, humidity, pressure, wind speed, and a weather icon.

