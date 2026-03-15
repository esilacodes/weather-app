import customtkinter as ctk
from api import get_weather

# Theme settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Weather App")
app.geometry("450x550")
app.resizable(False, False)

def search(event=None):
    city = entry.get()
    
    if city.strip() == "":
        result_label.configure(text="⚠️ Please enter a city name!", text_color="orange")
        return
    
    data = get_weather(city)
    
    if data:
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        city_name = data["name"]
        
        result_label.configure(
            text_color="white",
            text=(
                f"📍 {city_name}\n\n"
                f"🌡  Temperature: {temp}°C\n"
                f"🤔 Feels like: {feels_like}°C\n"
                f"🌤  Status: {desc}\n"
                f"💧 Humidity: {humidity}%\n"
                f"💨 Wind: {wind} m/s"
            )
        )
    else:
        result_label.configure(text="X City not found!", text_color="red")

# Title
title = ctk.CTkLabel(app, text="🌍 Weather App", font=("Arial", 28, "bold"))
title.pack(pady=30)

# Search frame
frame = ctk.CTkFrame(app, fg_color="transparent")
frame.pack(pady=10)

entry = ctk.CTkEntry(frame, placeholder_text="Enter city name...", width=280, height=45, font=("Arial", 14))
entry.pack(side="left", padx=10)
entry.bind("<Return>", search)

button = ctk.CTkButton(frame, text="Search", width=80, height=45, font=("Arial", 14), command=search)
button.pack(side="left")

# Result box
result_frame = ctk.CTkFrame(app, width=380, height=220, corner_radius=15)
result_frame.pack(pady=30)
result_frame.pack_propagate(False)

result_label = ctk.CTkLabel(result_frame, text="Search for a city...", font=("Arial", 15), justify="left")
result_label.pack(expand=True)

app.mainloop()