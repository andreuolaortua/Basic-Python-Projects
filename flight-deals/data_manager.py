import requests

GOOGLE_SHEET_ENDPOINT = "https://api.sheety.co/55131ae65e36ae087270d390b649cbbf/copiaDeFlightDeals/prices/2"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    #This class is responsible for talking to the Google Sheet.
    def get_price(self):

        response = requests.get(url=GOOGLE_SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data


    def set_price(self):

        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)