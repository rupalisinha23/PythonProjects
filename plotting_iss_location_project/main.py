#!/bin/python3

import json
import turtle
import urllib.request


# fetching the iss information which is publicly available
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())


print('People in space currently: ', result['number'], '\nNames are: ')
for people in result['people']:
    print(people['name'])

# fetching the current coordinates of iss
url_iss = 'http://api.open-notify.org/iss-now.json'
response_iss = urllib.request.urlopen(url_iss)
result_iss = json.loads(response_iss.read())
lat = result_iss['iss_position']['latitude']
lon = result_iss['iss_position']['longitude']

# plotting the coordinates of the iss on the nasa available world map
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.jpg')

screen.register_shape('iss.png')
iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)
iss.penup()
iss.goto(lon,lat)
