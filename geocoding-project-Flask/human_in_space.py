from dotenv import dotenv_values
import requests
import json

# Assignment: 

# Factor in another tab or functionality into your ISS app that displays the current people in space 
# (http://open-notify.org/Open-Notify-API/People-In-Space/). This can be done on the same page, or a 
# separate route (preferably a separate route)

ENV = dotenv_values()

req = requests.get(ENV['URL_HumansSpace'])
response = req.json()

print ('PEOPLE IN SPACE RIGHT NOW:\n')
print(f"There is {response['number']} people in space right now:")
for i in response['people']:
    print (' - ',i['name'])
