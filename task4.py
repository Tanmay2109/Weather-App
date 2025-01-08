#Project by Tanmay Manish Patil
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from PIL import Image, ImageTk

# OpenWeatherMap API Key
API_KEY = 'fcc8de7015bbb202209bbf0261babf4c'  # Replace with your own OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/"

# Initialize Tkinter root window
root = tk.Tk()
root.title("Weather App")
root.geometry("600x600")
root.config(bg="#4E91A1")  # Set a background color

# Use a stylish font for labels and text
font_header = ("Helvetica", 20, "bold")
font_info = ("Helvetica", 14)
font_button = ("Helvetica", 12, "bold")

# Function to get weather data
def get_weather(city=None):
    # Get the city name either from input or use geolocation
    if city:
        location = city
    else:
        location = location_entry.get()

    if not location:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    try:
        # Request current weather data
        current_weather_url = f"{BASE_URL}weather?q={location}&appid={API_KEY}&units=metric"
        response = requests.get(current_weather_url)
        data = response.json()

        if data['cod'] != 200:
            messagebox.showerror("Error", f"City '{location}' not found.")
            return

        # Extract relevant weather data
        city_name = data['name']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        weather_desc = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        weather_icon = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{weather_icon}.png"

        # Update the UI with the weather data
        city_label.config(text=f"{city_name}")
        temperature_label.config(text=f"Temperature: {temp}°C")
        description_label.config(text=f"Description: {weather_desc.capitalize()}")
        humidity_label.config(text=f"Humidity: {humidity}%")
        pressure_label.config(text=f"Pressure: {pressure} hPa")
        wind_speed_label.config(text=f"Wind Speed: {wind_speed} m/s")
        
        # Display weather icon
        img = Image.open(requests.get(icon_url, stream=True).raw)
        img = img.resize((100, 100))  # Resize image
        weather_icon_image = ImageTk.PhotoImage(img)
        icon_label.config(image=weather_icon_image)
        icon_label.image = weather_icon_image  # Keep a reference

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Error fetching weather data: {e}")
    except GeocoderTimedOut:
        messagebox.showerror("Error", "Geocoding service timed out. Please try again later.")

# Function to get the current location of the user
def get_location():
    try:
        geolocator = Nominatim(user_agent="weather_app")
        location = geolocator.geocode("Me", timeout=10)
        if location:
            get_weather(location.address)
        else:
            messagebox.showwarning("Location Error", "Could not retrieve your location.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while getting location: {e}")

# UI Elements - Using Frames for better organization
header_frame = tk.Frame(root, bg="#4E91A1")
header_frame.pack(pady=10, fill="x")

city_label = tk.Label(header_frame, text="Enter City Name", font=font_header, bg="#4E91A1", fg="white")
city_label.pack()

# Entry for the location
location_entry = tk.Entry(root, font=font_info, width=30, justify="center")
location_entry.pack(pady=10)

# Buttons - Get Weather and Use Current Location
button_frame = tk.Frame(root, bg="#4E91A1")
button_frame.pack(pady=20, fill="x")

get_weather_button = tk.Button(button_frame, text="Get Weather", font=font_button, command=get_weather, bg="#F1D302", fg="black", relief="raised", width=20)
get_weather_button.pack(side="left", padx=10)

current_location_button = tk.Button(button_frame, text="Use Current Location", font=font_button, command=get_location, bg="#F1D302", fg="black", relief="raised", width=20)
current_location_button.pack(side="right", padx=10)

# Weather Details - Labels to show temperature, humidity, and other details
weather_frame = tk.Frame(root, bg="#F8F8F8")
weather_frame.pack(pady=20, fill="both", expand=True)

temperature_label = tk.Label(weather_frame, text="Temperature: ", font=font_info, bg="#F8F8F8", anchor="w")
temperature_label.pack(fill="x", padx=20, pady=5)

description_label = tk.Label(weather_frame, text="Description: ", font=font_info, bg="#F8F8F8", anchor="w")
description_label.pack(fill="x", padx=20, pady=5)

humidity_label = tk.Label(weather_frame, text="Humidity: ", font=font_info, bg="#F8F8F8", anchor="w")
humidity_label.pack(fill="x", padx=20, pady=5)

pressure_label = tk.Label(weather_frame, text="Pressure: ", font=font_info, bg="#F8F8F8", anchor="w")
pressure_label.pack(fill="x", padx=20, pady=5)

wind_speed_label = tk.Label(weather_frame, text="Wind Speed: ", font=font_info, bg="#F8F8F8", anchor="w")
wind_speed_label.pack(fill="x", padx=20, pady=5)

# Weather icon label
icon_label = tk.Label(root, bg="#F8F8F8")
icon_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
