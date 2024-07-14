import requests

def find_temperature():
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

    results = []

    for x in response['data']:
        results.append(x['city_name'])
        results.append(str(x['temp']))
    
    return results