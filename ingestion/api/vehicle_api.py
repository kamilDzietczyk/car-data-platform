import requests

API_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"

def fetch_vehicle_makes():

    response = requests.get(API_URL)
    data = response.json()

    return data["Results"]