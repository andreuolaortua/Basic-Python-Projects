import requests
from flight_data import FlightData

import kiwi
import datatime
KIWI_ENDPOINT = ""
TEQUILA_ENDPOINT = ""
API_KEY = ""

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_destination = {}

    def get_destination_code(self, city_name):

        headers = {
            "apikey": API_KEY
        }
        query = {
            "term": city_name,
            "location_types": "city"
            }
        location_endpoint = requests.get(url=TEQUILA_ENDPOINT, headers=headers, params=query)
        data = location_endpoint.json()["locations"]
        code = data[0]["code"]
        return code




    def check_flights(self, origin_city_code, destination_city_code, out_date, return_date):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=headers, params=query)

        try:
            data = requests.json()["data"][0]
        except IndexError
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

