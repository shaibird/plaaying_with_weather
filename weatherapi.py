import requests
import pandas as pd
import yaml 
from requests.models import LocationParseError
import os

#file containing location data and credtentials 
file = 'config.yaml'

#opening the yaml file in read mode, redefining file as f
with open(file, 'r') as f:
    config = yaml.safe_load(f)

locations = config['crags']

#visualizing data from yaml file being put in its place.
#for key,values in locations.items():
    #print(f'Location is: {key}')
    #print(f"\tLatitude is: {values['lat']}")
    #print(f"\tLongitude is {values['lon']}")

#API KEY
api_key = config['credentials']['api_key']
url = "http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&exclude=hourly,minutely,alerts&appid={api_key}"

# initialize vars
results_dict = {}
session = requests.Session()

#iterate through all locations and pass args into URL
current_weather = {}

for key, values in locations.items():
    form_url = url.format( 
        lat=values['lat'],
        lon=values['lon'],
        api_key=api_key
        )

    result = session.get(form_url)
    result_json = result.json()
    
    current_weather[key] = result_json['main']
    print (f'{key} weather collected')

pd.DataFrame(current_weather).T

# int(results_dict['Stone Fort / Little Rock City']['main']['temp'])

print(current_weather)

for weather in current_weather:
    print(int(['main']['temp']))



