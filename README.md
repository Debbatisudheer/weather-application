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



Algorithm
=========

The algorithm used in the weather application is straightforward:
-----------------------------------------------------------------

    Fetch Weather Data: The application sends an HTTP GET request to the OpenWeatherMap API to fetch weather data for a specified city.
    Parse Response: It then parses the JSON response received from the API to extract relevant weather information such as temperature, humidity, and wind speed.
    Display Weather Information: Finally, it displays the fetched weather information to the user.

Data Structures:
----------------

    Dictionary: The JSON response from the API is parsed into a Python dictionary (data) for easy access to weather information. For example, data["main"]["temp"] accesses the temperature value.

Python Topics Used:
===================

    HTTP Requests (requests library):
        The requests library is used to send HTTP GET requests to the OpenWeatherMap API and handle the API response.
    Exception Handling:
        try-except blocks are used for error handling. Exceptions like network errors or API errors are caught and appropriate error messages are displayed to the user.
    User Input:
        input() function is used to prompt the user to enter the city name for which they want to fetch weather information.
    String Formatting:
        F-strings (formatted string literals) are used for formatting error messages and displaying weather information.
    Conditional Statements:
        if-else statements are used to check the status code of the API response and handle errors accordingly.
    Functions:
        Modular programming is used with functions like fetch_weather() to fetch weather data and display_weather() to display weather information.
    Main Function:
        The script is structured with a main function (main()) that orchestrates the execution of the application.

Additional Topics:
=================

    API Integration:
        Incorporated an external API (OpenWeatherMap) to fetch weather data.
    JSON Parsing:
        Parsed JSON responses from the API to extract relevant weather information.
    Module Importing:
        Imported the requests library for making HTTP requests to the API.

Time Complexity:
----------------

    API Request: The time complexity of making an API request depends on the efficiency of the network communication and the processing time on the server side. Generally, it's considered constant time (O(1)) from the perspective of the client application.
    JSON Parsing: The time complexity of parsing a JSON response depends on the size of the response and the complexity of the JSON structure. In most cases, it's considered linear time (O(n)), where n is the number of elements in the JSON response.
    Displaying Weather Information: Displaying weather information involves simple print statements and accessing dictionary values, which are constant-time operations (O(1)).

Overall, the time complexity of the application is dominated by the API request and JSON parsing, both of which typically operate in linear time (O(n)).

Space Complexity:
----------------

    API Response: The space complexity of storing the API response depends on the size of the response data. If we consider the parsed JSON response stored in memory, the space complexity is linear (O(n)), where n is the number of elements in the JSON response.
    Variables: The space complexity of storing variables such as city name, API key, and parameters used in the API request is constant (O(1)).
    Function Calls: Function calls consume memory for local variables and function call stacks. However, in this application, the function call depth is constant and doesn't depend on the input size, so it's also constant space (O(1)).

Overall, the space complexity of the application is primarily determined by the size of the API response data, making it linear (O(n)).
Conclusion:

    Time Complexity: Generally linear (O(n)) due to API request and JSON parsing.
    Space Complexity: Primarily linear (O(n)) due to storing the API response data.

These complexities are typical for applications that interact with external APIs and process data in JSON format.

API Reference
-------------

https://home.openweathermap.org

Contributing
------------

Contributions to the Weather Application are welcome! You can contribute by:
----------------------------------------------------------------------------

    Reporting bugs
    Suggesting new features
    Submitting pull requests

License
-------

This project is licensed under the MIT License.


Contact
-------

For any inquiries or feedback, please contact:

    Email: debbatisudheerpatel@gmail.com
    
