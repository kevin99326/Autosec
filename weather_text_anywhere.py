import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import os

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

def dic_to_string(dictionary_value):
    return ("Main : "  + str(dictionary_value["weather"][0]["main"]) +"\n"
    + "Description : " + str(dictionary_value["weather"][0]["description"]) + "\n"
    + "Temperature : " + str(dictionary_value["main"]["temp"]) + "\n"
    + "Humidity : " + str(dictionary_value["main"]["humidity"]) + "\n"
    + "Minimum Temperature : " + str(dictionary_value["main"]["temp_min"]) + "\n"
    + "Maximum Temperature : " + str(dictionary_value["main"]["temp_max"]))

def get_weather_dictionary(api_key, city_id='6176823'):
    """Request the weather from OpenWeatherMap
    
    Request the weather for a city, using its city_id, from OpenWeatherMap 
    using the provided api_key. Process the response object assuming it is
    valid JSON and return a Python dictionary version of that JSON.
    Parameters
    ----------
    api_key: str
        A valid API key for OpenWeatherMap in the form of a string
    city_id: str, optinal
        A number from OpenWeatherMap's city id list passed as a string. 
        Defaults to Waterloo Canada.
    Returns
    -------
    resp: dict
        Processed response from server; interpreted as JSON and turned into a
        Python dictionary.
    """
    payload = {'id': city_id, 'appid': api_key, 'units': 'metric'}
    
    raw_resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    resp = raw_resp.json()
    return resp



# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC66f4fbb5332c8512bb6af91bdd83ceed'
auth_token = '242cf642c5be16136ef718795fc0dc9b'
client = Client(account_sid, auth_token, http_client=proxy_client) # Notice the keyword argument


message = client.messages \
                .create(
                     body=dic_to_string(get_weather_dictionary('27c560d3302657be7e329c35fabe9e8d', city_id='6176823')),
                     from_='+16475593094',
                     to='+16478610846'
                 )

print(message.sid)

