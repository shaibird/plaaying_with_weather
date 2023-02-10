import requests
import json
import datetime, pytz
import pandas as pd

key = '5cc8f9a3748e9d010417fea83ff5784f'
Location = 'Stone Fort'
lat = '35.247716'
lon = '-85.21987'
url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&&appid={key}'
#stores the JSON response
response = requests.get(url)
data = response.json()

#checking the statues of the code request
#if response.status_code == 200:
    #getting data from list 
    #main = data['daily']
    

#changing time from epoch to human
for index in range(1,8):
    local_time = datetime.datetime.fromtimestamp( data['daily'][index]['dt'] , tz=pytz.timezone('US/Eastern'))
    str_time = local_time.strftime( '%Y-%m-%d %a')
    print( f" Day [+{index}] {str_time} =  {data['daily'][index]['dt']} = {data['daily'][index]['temp']['day']}")

datetime.datetime.fromtimestamp(data['daily'][0]['dt'])

# normalize json into tabular form
df = pd.json_normalize(data['daily'])

# fuzzy match date cols
dt_cols = ['dt', 'sun','moon']

# format datetime cols
for dt_col in dt_cols:
    for col in df.columns:
        if col.startswith(dt_col):
            df[col] = pd.to_datetime(df[col], unit='s')

# remove dot notation
df.columns = df.columns.str.replace('.','_', regex=False)

df.loc[df.dt >= datetime.datetime.today()]