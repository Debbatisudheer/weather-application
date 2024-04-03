import requests

def fetch_weather(city):
    api_key = '40210a6ba2b51e573627c77b0758af3a'  # Use your API key here
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    forecast_url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}

    try:
        current_response = requests.get(base_url, params=params)
        forecast_response = requests.get(forecast_url, params=params)

        current_data = current_response.json()
        forecast_data = forecast_response.json()

        if current_response.status_code == 200 and forecast_response.status_code == 200:
            return current_data, forecast_data
        else:
            print(f'Error: {current_data.get("message", "Unknown error")} (Current) | {forecast_data.get("message", "Unknown error")} (Forecast)')
            return None, None
    except Exception as e:
        print(f'Error fetching weather: {e}')
        return None, None

def display_weather(current_data, forecast_data):
    if current_data and forecast_data:
        print(f'Current Weather in {current_data["name"]}:')
        print(f'Temperature: {current_data["main"]["temp"]}°C')
        print(f'Humidity: {current_data["main"]["humidity"]}%')
        print(f'Wind Speed: {current_data["wind"]["speed"]} m/s')

        print('\nWeather Forecast for the next few days:')
        for forecast in forecast_data['list']:
            date_time = forecast['dt_txt']
            temperature = forecast['main']['temp']
            print(f'{date_time}: {temperature}°C')

    else:
        print('Weather data not available.')

def main():
    city = input('Enter city name: ')
    current_weather, weather_forecast = fetch_weather(city)
    display_weather(current_weather, weather_forecast)

if __name__ == "__main__":
    main()