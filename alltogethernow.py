import requests
import pandas as pd
import yaml
import requests.models
from datetime import datetime
import json

#fetch and display weather info
def time_format(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()


#file containing location info and credentials
file = 'config.yaml'

#opening the yaml file in read mode
with open(file, 'r') as f:
    config = yaml.safe_load(f)

#in yaml file, defining the crag 
locations = config['crags']
api_key = config['credentials']['api_key']

for key,values in locations.items():
    lat = values['lat']
    lon = values['lon']

url = 'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=imperial&exclude=hourly,alerts,minutely&appid={api_key}'

#initializing vars
results_dict = {}
data = requests.Session()

for key, values in locations.items():
    form_url = url.format(
        lat = values['lat'],
        lon = values['lon'],
        api_key = api_key
    ) 

    results = data.get(form_url)
    results_dict[key] = results.json()
    print(f'{key} weather collected')
    print(results_dict)



#dayday dataman code 
# # normalize json into tabular form
# df = pd.json_normalize(data['daily'])

# # fuzzy match date cols
# dt_cols = ['dt', 'sun','moon']

# # for each area, normalize json into a DataFrame
# dfs = {}
# for area, info in results_dict.items():
#     dfs[area] = pd.json_normalize(info['daily'])



# # format all datetime cols
# for df in dfs.values():
#     # format datetime cols
#     for dt_col in dt_cols:
#         for col in df.columns:
#             if col.startswith(dt_col):
#                 df[col] = pd.to_datetime(df[col], unit='s')


# # add crag key name as df col
# for k,v in dfs.items():
#     v['crag'] = k

# # combine into master
# master = pd.concat(dfs.values())


# # remove dot notation
# df.columns = df.columns.str.replace('.','_', regex=False)

# df.loc[df.dt >= datetime.datetime.today()]