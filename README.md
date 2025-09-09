					WEATHER DATA FETCHER
A simple desktop application that fetches and displays current weather data for any city using the OpenWeatherMap API. The app is built with Python and customtkinter for a modern, user-friendly graphical interface.

					FEATURES
Fetches real-time weather data (temperature and description).
Simple and intuitive graphical user interface.
Includes robust error handling for network issues and invalid city names.
Follows best practices for API key security by using environment variables.

					GETTING STARTED
Follow these steps to set up and run the application on your local machine.

1. Prerequisites
Make sure you have Python installed. You can download it from python.org.

2. Installation
Install the required libraries using pip.

pip install customtkinter
pip install requests
python -m pip install python-dotenv

3. Set Up Your API Key (Crucial Step)
For security, the API key is not stored directly in the code. You will need to obtain your own key and store it in a secure location.

Get an API Key:

Sign up for a free account on the OpenWeatherMap website.

Go to the "API keys" tab to find your personal API key.

Create a .env file:

In the same folder as your weather_app.py file, create a new file named .env.

Add the following line to the file, replacing your_api_key_here with your actual key:

OPENWEATHER_API_KEY=your_api_key_here

Note: The .env file is a standard way to store environment-specific variables. It is automatically ignored by Git (using a .gitignore file), which prevents you from accidentally uploading your key to GitHub.

4. Running the Application
Once your .env file is set up, you can run the application from your terminal.

python weather_app.py

Usage
The application window will appear.

Type the name of a city into the input field.

Click the "Get Weather" button to see the results.

Contributing
If you have suggestions for improvements or want to add a new feature, feel free to open an issue or submit a pull request!