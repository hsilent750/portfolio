import customtkinter as ctk
import requests
import math
import os  # Import the os module to access environment variables

# Define your main application class
class App(ctk.CTk):
    def __init__(self):
        # Call the constructor of the parent class (CTk)
        super().__init__()

        # GUI setup
        self.title('Weather App')
        self.geometry('500x300')
        self.configure(bg_color="white")

        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('dark-blue')

        # Get the API key from an environment variable for security
        # This is a best practice to avoid exposing sensitive keys on GitHub
        self.api_key = os.getenv("OPENWEATHER_API_KEY")

        if not self.api_key:
            print("Error: OPENWEATHER_API_KEY not found in environment variables.")
            print("Please follow the instructions in the README.md file to set it up.")
            # Set a placeholder and disable functionality if key is missing
            self.result_label_text = "API key not found. Check your environment setup."
            self.fetch_button_state = "disabled"
        else:
            self.result_label_text = ""
            self.fetch_button_state = "normal"


        self.frame = ctk.CTkFrame(self)
        self.frame.pack(pady=20, padx=40, expand=True, fill='both')

        # Title Label
        self.title_label = ctk.CTkLabel(
            self.frame,
            text="City Weather",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.title_label.pack(pady=(10, 20))

        # City input field
        self.city_entry = ctk.CTkEntry(
            self.frame,
            placeholder_text="Enter City Name",
            width=200
        )
        self.city_entry.pack(pady=(0, 10))

        # Button to fetch weather data
        self.fetch_button = ctk.CTkButton(
            self.frame,
            text="Get Weather",
            command=self.weather_status,
            state=self.fetch_button_state
        )
        self.fetch_button.pack(pady=(0, 20))

        # Label to display the weather result
        self.result_label = ctk.CTkLabel(
            self.frame,
            text=self.result_label_text,
            font=ctk.CTkFont(size=16)
        )
        self.result_label.pack()

    # Define weather_status as a method of the class
    def weather_status(self):
        city = self.city_entry.get()
        if not city:
            self.result_label.configure(text="Please enter a city name.")
            return

        # Check if the API key is available
        if not self.api_key:
            self.result_label.configure(text="Error: API key not configured.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"

        try:
            response = requests.get(url).json()

            # Check the response status code
            if response.get("cod") == 200:
                temp_kelvin = response["main"]["temp"]
                temp_celsius = math.floor(temp_kelvin - 273.15)
                weather_desc = response["weather"][0]["description"].capitalize()

                # Update the result label with the fetched data
                self.result_label.configure(
                    text=f"Weather in {city}:\n{temp_celsius}°C, {weather_desc}"
                )
            else:
                # Handle API errors (e.g., city not found)
                error_message = response.get("message", "An unknown error occurred.")
                self.result_label.configure(text=f"Error: {error_message}")

        except requests.exceptions.RequestException:
            # Handle network-related errors
            self.result_label.configure(text="Network Error: Could not connect to the API.")


# Create an instance of the class and run the main loop
if __name__ == "__main__":
    app = App()
    app.mainloop()
