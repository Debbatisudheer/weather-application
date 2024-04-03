Python Weather App Documentation
=========================

Introduction:
--------------
The Weather App is a simple Python script that fetches current weather information and weather forecast for a given city using the OpenWeatherMap API.

Features
--------

    1. Fetches current weather data for a specified city.
    2. Displays temperature, humidity, and wind speed information.
    3. Provides error handling for network issues and API errors.

Usage:
-------
To use the Weather App, follow these steps:
1. Run the script in a Python environment.
2. Enter the name of the city for which you want to fetch weather information when prompted.

Dependencies:
---------------
This script requires the `requests` library to make HTTP requests to the OpenWeatherMap API. You can install it using pip:

Functionality:
----------------
1. `fetch_weather(city)`: This function takes the name of a city as input and fetches current weather information and weather forecast for that city from the OpenWeatherMap API. It returns two JSON objects containing the current weather data and weather forecast data respectively.

2. `display_weather(current_data, forecast_data)`: This function takes the current weather data and weather forecast data as input and displays the information to the user. It prints the current temperature, humidity, wind speed, and the weather forecast for the next few days.

3. `main()`: This function serves as the entry point of the script. It prompts the user to enter the name of a city, fetches weather data using `fetch_weather()`, and displays the information using `display_weather()`.

Error Handling:
------------------
The script handles errors that may occur during the process of fetching weather data. If an error occurs, it prints an error message indicating the nature of the error.

API Key:
----------
The script requires an API key to access the OpenWeatherMap API. The API key should be stored in the `api_key` variable within the script.

Note:
------
Before using the Weather App, ensure that you have a valid API key for the OpenWeatherMap API. You can obtain an API key by signing up on the OpenWeatherMap website (https://home.openweathermap.org/users/sign_up).

Web Weather App Documentation
=========================

Introduction:
--------------
The Weather App is a simple web application that allows users to fetch current weather information for a specific city using the OpenWeatherMap API. This HTML page provides the user interface for the application.

Usage:
-------
To use the Weather App, follow these steps:
1. Open the HTML page in a web browser.
2. Enter the name of the city for which you want to fetch weather information in the input field provided.
3. Click the "Get Weather" button to fetch and display the weather information for the specified city.

Dependencies:
---------------
This HTML page does not have any external dependencies. However, it relies on the OpenWeatherMap API to fetch weather data, so an internet connection is required.

Functionality:
----------------
1. `fetchWeather()`: This JavaScript function is called when the user clicks the "Get Weather" button. It retrieves the value entered in the input field (city name), constructs the API URL with the city name and API key, and makes a fetch request to the OpenWeatherMap API. Upon receiving a response, it parses the JSON data and updates the weather information displayed on the page.

2. Display Weather Information: The weather information fetched from the OpenWeatherMap API is displayed on the page in the designated div element ('weather-info'). If the city is found (HTTP status code 200), the current temperature, humidity, and wind speed are displayed. If the city is not found, an error message is displayed.

Error Handling:
------------------
The script handles errors that may occur during the process of fetching weather data. If an error occurs, it logs the error to the console and displays an error message to the user.

API Key:
----------
The Weather App requires an API key to access the OpenWeatherMap API. The API key should be stored in the `apiKey` variable within the JavaScript code.

Note:
------
Before using the Weather App, ensure that you have a valid API key for the OpenWeatherMap API. You can obtain an API key by signing up on the OpenWeatherMap website (https://home.openweathermap.org/users/sign_up).
