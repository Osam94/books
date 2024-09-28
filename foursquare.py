import requests
import json

def get_places(category):
    url = "https://api.foursquare.com/v3/places/search"
    params = {
        "client_id": "client_id",
        "client_secret": "client_secret",
        "near": "москва",
        "query": category,
        "limit": 50
    }
    headers = {
        "Accept": "application/json",
        "Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
    }

    response = requests.get(url=url, params=params, headers=headers)
    data = response.json()

    if 'results' in data:
        return data['results']
    else:
        return []

def main():
    category = input("Enter a category: ")
    places = get_places(category)

    for place in places:
        print(place['name'])

if __name__ == "__main__":
    main()





