import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    api_key = "e557329cfb85db3b52ccfdeb69f1737d"  # Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = city_entry.get()
    complete_url = f"{base_url}q={city}&appid={api_key}"

    try:
        response = requests.get(complete_url)
        data = response.json()
        if data["cod"] != "404":
            main_data = data["main"]
            weather_data = data["weather"][0]

            temperature = main_data["temp"] - 273.15  # Convert temperature to Celsius
            humidity = main_data["humidity"]
            description = weather_data["description"]

            result_label.config(text=f"Temperature: {temperature:.2f}°C\nHumidity: {humidity}%\nWeather: {description}")
        else:
            messagebox.showerror("Error", "City not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
app = tk.Tk()
app.title("Weather Forecast")

# Create an input field for the city
city_label = tk.Label(app, text="Enter City:")
city_label.pack()
city_entry = tk.Entry(app)
city_entry.pack()

# Create a button to get weather data
get_weather_button = tk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack()

# Create a label to display weather data
result_label = tk.Label(app, text="", justify="left")
result_label.pack()

app.mainloop()
