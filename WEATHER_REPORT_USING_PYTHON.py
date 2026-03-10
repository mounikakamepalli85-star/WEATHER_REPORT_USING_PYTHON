import tkinter as tk
from tkinter import messagebox
import requests
API_KEY = "419dd015af23fab43e0fef1d5dc5126b"  

def get_weather():
    city = city_entry.get().strip()

    if not city:
        messagebox.showerror("Error", "Please enter city name")
        return

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": f"{city},IN",
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)


        if response.status_code == 401:
            messagebox.showerror("API Error", "Invalid or Inactive API Key.\nVerify email & wait 10 minutes.")
            return

        if response.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return

        response.raise_for_status()

        data = response.json()

        # Extract weather data safely
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        city_name = data["name"]

        # Update UI
        city_label.config(text=city_name)
        temp_label.config(text=f"{temperature} °C")
        desc_label.config(text=description)
        humidity_label.config(text=f"{humidity} %")
        pressure_label.config(text=f"{pressure} hPa")
        wind_label.config(text=f"{wind_speed} m/s")

    except requests.exceptions.ConnectionError:
        messagebox.showerror("Network Error", "Check your internet connection")

    except requests.exceptions.Timeout:
        messagebox.showerror("Timeout", "Server took too long to respond")

    except Exception as e:
        messagebox.showerror("Error", f"Unexpected Error:\n{str(e)}")

root = tk.Tk()
root.title("Weather Report - India")
root.geometry("950x520")
root.configure(bg="#1e3c72")
root.resizable(False, False)

# Left Panel
left_frame = tk.Frame(root, bg="black", padx=25, pady=25)
left_frame.place(x=80, y=100)

city_entry = tk.Entry(left_frame, font=("Arial", 14), width=25)
city_entry.pack(pady=10)

search_button = tk.Button(
    left_frame,
    text="Search",
    font=("Arial", 12),
    command=get_weather
)
search_button.pack(pady=5)

city_label = tk.Label(
    left_frame,
    text="City",
    font=("Arial", 22, "bold"),
    fg="white",
    bg="black"
)
city_label.pack(pady=10)

temp_label = tk.Label(
    left_frame,
    text="-- °C",
    font=("Arial", 45, "bold"),
    fg="white",
    bg="black"
)
temp_label.pack()

desc_label = tk.Label(
    left_frame,
    text="Weather",
    font=("Arial", 16),
    fg="white",
    bg="black"
)
desc_label.pack()

# Right Panel
right_frame = tk.Frame(root, bg="black", padx=25, pady=25)
right_frame.place(x=600, y=130)

tk.Label(right_frame, text="Humidity",
         fg="white", bg="black",
         font=("Arial", 12)).pack(pady=5)

humidity_label = tk.Label(right_frame,
                          text="--",
                          fg="white", bg="black",
                          font=("Arial", 12))
humidity_label.pack()

tk.Label(right_frame, text="Pressure",
         fg="white", bg="black",
         font=("Arial", 12)).pack(pady=5)

pressure_label = tk.Label(right_frame,
                          text="--",
                          fg="white", bg="black",
                          font=("Arial", 12))
pressure_label.pack()

tk.Label(right_frame, text="Wind Speed",
         fg="white", bg="black",
         font=("Arial", 12)).pack(pady=5)

wind_label = tk.Label(right_frame,
                      text="--",
                      fg="white", bg="black",
                      font=("Arial", 12))
wind_label.pack()
footer_label = tk.Label(
    root,
    text="Created by Mounika K",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e3c72"
)
footer_label.pack(side="bottom", pady=10)


root.mainloop()