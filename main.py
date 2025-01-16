import requests
import json
apikey=input('Enter your api key: ')
city=input('Enter the name of the city: ')
try:
    r=requests.get(f'https://api.weatherapi.com/v1/current.json?key={apikey}&q={city}')

    dict=json.loads(r.text)
    w=(dict['current']['temp_c'])
    name=dict['location']['name']
    region=dict['location']['region']
    country=dict['location']['country']
    print(f'Name : {name}')
    print(f'Region : {region}')
    print(f'Country : {country}')

    print(f'The current temperature in {city} is {w} °C')
except Exception as e:
    print('Some Error Occurred!')
    print(f'Error Details: {e}')