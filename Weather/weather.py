from Config import config
import requests
import json

key = config.weather_key
exclude = 'minutely, hourly'
units = 'imperial'


def get_location(person: tuple) -> tuple:
    zip_code = person['zip_code']
    country_code = person['country_code']
    location = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={key}'
    location = json.loads(requests.get(location).text)
    latitude, longitude = location.get('lat'), location.get('lon')
    return latitude, longitude


def get_weather(person: tuple) -> dict:
    lat, lon = get_location(person)
    weather_conditions = {}
    weather = f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&units={units}&appid={key}'
    weather = json.loads(requests.get(weather).text)
    current = weather.get('current')
    print(''.join(str(round(current.get('temp'))) + '°'))
    return weather_conditions




