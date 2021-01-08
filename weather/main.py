import requests
import os

OWN_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall'
api_key = os.environ.get('api_key')

weather_params = {
    "lat": 46.644371,
    "lon": 7.5168752,
    "appid": api_key,
}

response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It`s going to rain today. Remenber to bring an umbrella")
else:
    print('Its not to going rain today.')
