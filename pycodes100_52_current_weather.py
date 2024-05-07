#https://newdigitals.org/2024/02/24/100-basic-python-codes/#current-weather
#Current Weather
#Find current weather of any city using OpenWeatherMap API with your API key
# importing requests and json
import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
#City Name 
CITY = "Amsterdam"
# API key 
API_KEY = "YOUR_API_KEY"
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']-273.15
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   print(f"{CITY:-^30}")
   print(f"Temperature: {temperature}")
   print(f"Humidity: {humidity}")
   print(f"Pressure: {pressure}")
   print(f"Weather Report: {report[0]['description']}")
else:
   # showing the error message
   print("Error in the HTTP request")

#Example I/O
----------Amsterdam-----------
Temperature: 9.720000000000027
Humidity: 82
Pressure: 1020
Weather Report: broken clouds
