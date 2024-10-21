''' GEOCODE
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/google/geocode?location=syracuse' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 6502ef18c563ffdc99b1bc4c'
'''

''' WEATHER
curl -X 'GET' \
  'https://cent.ischool-iot.net/api/weather/current?units=imperial&lon=-78&lat=43' \
  -H 'accept: application/json' \
  -H 'X-API-KEY: 6502ef18c563ffdc99b1bc4c'
'''

import requests
import streamlit as st

st.title("Weather⛅️")
location = st.text_input("Enter a location")
if st.button("Get Weather"):
    url = "https://cent.ischool-iot.net/api/google/geocode"
    querystring = {"location":location}
    headers = {'X-API-KEY': '6502ef18c563ffdc99b1bc4c'}
    response = requests.get(url, params=querystring, headers=headers)
    response.raise_for_status()
    geocode = response.json()
    #st.write(geocode)
    lat = geocode['results'][0]['geometry']['location']['lat']
    lon = geocode['results'][0]['geometry']['location']['lng']
    url = "https://cent.ischool-iot.net/api/weather/current"
    querystring = {"units":"imperial","lon":lon,"lat":lat}
    response = requests.get(url, params=querystring, headers=headers)
    response.raise_for_status()
    weather = response.json()
    st.write(weather)
    temp = weather['current']['temperature_2m']
    st.metric("Temperature", f"{temp}°F")
