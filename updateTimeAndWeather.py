#!/usr/bin/python
# importing the requests library 
import I2C_LCD_driver
from time import *
import sys
import requests 
import json
import datetime

# api-endpoint 
URL = "https://api.openweathermap.org/data/2.5/weather?zip={your_zip_code_here},us&appid={insert_your_app_id_here}&units=imperial" 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL) 
  
# extracting data in json format 
data = r.json() 

# Make sure HTTP response code is 200, which means the request to the API was fine.
if ((r.status_code) == 200 and (data['cod'] == 200)) :
        # set the temperature to the temp variable
	temp = round(data['main']['temp'])
        # set the feels like temperature to the perceivedTemperature variable
	perceivedTemperature = round(data['main']['feels_like'])
        # set the weather description (e.g. cloudy) to the variable desc
	desc = data['weather'][0]['main']
        # set the sunset to the variable sunset
	sunset = data['sys']['sunset']
        # set today's sunset  to the variable sunsetTime
	sunsetTime = datetime.datetime.fromtimestamp(sunset).strftime('%H:%M')
        # create a variable called weatherString which is used to output string that the LCD will display.
        # The commented out string was a little long for the screen, so I just showed the feels like temperature and descrption of today's weather 
	#weatherString = "Temp: {} Feels Like: ({}) {} Sunset: {} ".format(temp, perceivedTemperature, desc, sunsetTime)
	weatherString = "Temp: {} {}".format(perceivedTemperature, desc)
else:
        # If unable to grab the weather, then show No weather instead on the LCD. 
	weatherString = "No weather"

# Grab the current time from the device the code is running on.
# Most computers have an RTC or uses NTP to grab network time so theoretically, the time is usually accurate
currentDateTime = datetime.datetime.now()

# format the date and time to the full name of today (e.g. Monday) and the current hour in military time and minute
timeString = currentDateTime.strftime("%A %H:%M")

# Initiate the I2C_LCD code that controls the LCD
mylcd = I2C_LCD_driver.lcd()
# Clear out anything displayed on the LCD. This is done so that if let's say there was an 8 and now a 0,
# it actually shows 0, not 8
mylcd.lcd_clear()
# Write the current day, hour, and time to the first line of the LCD
mylcd.lcd_display_string(timeString, 1)
# Write the feels like temperature and weather descption to to the second line of the LCD
mylcd.lcd_display_string(weatherString, 2)



