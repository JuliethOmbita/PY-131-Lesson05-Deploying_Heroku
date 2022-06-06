import requests
from dotenv import dotenv_values

# Base Url for geocoding


ENV = dotenv_values()

address = input("Input the address: ")

#Your unique private_token should replace value of the private_token variable.
#To know how to obtain a unique private_token please refer the README file for this script.

data = {
    'key': ENV['PRIVATE_TOKEN'],
    'q': address,
    'format': 'json'
}
response = requests.get(ENV['URL'], params=data)

latitude = response.json()[0]['lat']
longitude = response.json()[0]['lon']

print(f"The latitude of the given address is: {latitude}")
print(f"The longitude of the given address is: {longitude}")
print("Thanks for using this script")