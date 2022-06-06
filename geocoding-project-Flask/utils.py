import requests as rqs

def get_coordinates (address, URL, PRIVATE_TOKEN):
    """ 
    Queries location API and get's coordinates
    """
    data = {
        'key': PRIVATE_TOKEN,
        'q': address,
        'format': 'json'
        }
    try:
        response = rqs.get(URL, params=data)
    except Exception as e:
        raise e

    lat = response.json()[0]['lat']
    lon = response.json()[0]['lon']

    return lat, lon