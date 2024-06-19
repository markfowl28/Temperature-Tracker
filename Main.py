import requests
from datetime import datetime
from DatabaseConnection import *

API_KEY = str("8f1ec676b7a4401a89ff427e761abd64")

# locates coordinates using ip address
my_ip_address = requests.get(f'http://api.ipify.org').text
location = requests.get(f'http://ip-api.com/json/{my_ip_address}').json()

latitude = location['lat']
longitude = location['lon']

# finds current temp using coordinates
response = requests.get(
    f"https://api.weatherbit.io/v2.0/current?"
    f"lat={latitude}&lon={longitude}&key={API_KEY}&units=I&include=minutely").json()

for x in response['data']:
    temp = (x['temp'])

# records time stamp for api call
now = datetime.now()
month = now.month
day = now.day
hour = now.hour
minute = now.minute

# passes temperature and time data to be added to database
add_data(temp=temp, month=month, day=day, hour=hour, minute=minute)
