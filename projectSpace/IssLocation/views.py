from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
from dotenv import dotenv_values
import requests


def say_hello(request):
    today = date.today()
    return HttpResponse(f"hello Julieth, {today}")


def ISSlocation(request):
    ENV = dotenv_values()
    req = requests.get(ENV['URL_ISS'])
    resp = req.json()
    data = {
        'key': ENV['PRIVATE_TOKEN'],
        'lat': resp['iss_position']['latitude'],
        'lon': resp['iss_position']['longitude'],
        'format': 'json'
    }
    loc_response = requests.get(ENV['URL_reverse_goe'], params=data)
    if loc_response:
        location = f"Over {loc_response.json()['address']['country']}"
    else:
        location = "ISS location can't be find"
    resp['location'] = location
    return render(request, "index.html", resp)


def humanInSpace(request):
    ENV = dotenv_values()
    reqHumans = requests.get(ENV['URL_HumansSpace'])
    respHumans = reqHumans.json()
    return render(request, "humans.html", respHumans)
