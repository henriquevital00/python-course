import requests
import gmaps

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

# Add google maps
#gmaps.configure(api_key='')
#gmaps.figure(center=(data['iss_position']['latitude'],
                     data['iss_position']['longitude']),
             zoom_level=12)

print(data)
