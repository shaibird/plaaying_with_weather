import requests
import json

key = '5cc8f9a3748e9d010417fea83ff5784f'
Location = 'Stone Fort'
lat = '35.247716'
lon = '-85.21987'
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=imperial&appid={key}'
#stores the JSON response
response = requests.get(url)
data = response.json()

# The current date we are interating through
current_date = ''

#checking the statues of the code request
if response.status_code == 200:
    #getting data from list 
    #main = data['list']
    # Iterates through the array of dictrionaries named list in the json_data
    for item in data['list']:

        # Time of the weather data recieved, partioned into 3 hour blocks
        time = item["dt_txt"]

        #Split the time into date and hour [2022-01-13 06:00:00]

