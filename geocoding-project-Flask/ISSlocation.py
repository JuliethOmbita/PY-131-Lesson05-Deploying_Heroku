from dotenv import dotenv_values
import requests
import json

# Exercise 1
# Write a python script that communicates with the following service Use the following API ISS Location: ISS Location (gives us the coordinates)
# Tells where the ISS is (Geographically)
#  Over JAPAN 
# HINT: You will have to use the Reverse Geocoding API of LocationIQ to get the address of where it is. REverse geocoding

# Exercise 2
# Turn the followings script above into a Flask or Django App of your choice.

ENV = dotenv_values()

req = requests.get(ENV['URL_ISS'])
response = req.json()

print ('International Space Station Current Location:\n')
print(f"The timestamp of this request is: {response['timestamp']}")
print(f"The latitude of ISS is: {response['iss_position']['latitude']}")
print(f"The longitude of ISS is: {response['iss_position']['longitude']}")
print("Thanks for using this script")

data = {
    'key': ENV['PRIVATE_TOKEN'],
    'lat': response['iss_position']['latitude'],
    'lon': response['iss_position']['longitude'],
    # 'lat': 40.671528499999994,
    # 'lon': -73.9514631477148,
    'format': 'json'
}
loc_response = requests.get(ENV['URL_reverse_goe'], params=data)
# print (loc_response.json())
if loc_response:
    print(f"Over {loc_response.json()['address']['country']}")
else: 
    print ("ISS location can't be find")
    

