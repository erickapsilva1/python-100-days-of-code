import requests
from flight_data import FlightData

API_FLIGHT_SEARCH_ENDPOINT = ""
API_FLIGHT_API_KEY = ""

class FlightSearch:

    def get_code(self, city_name):
        location_endpoint = f"{API_FLIGHT_SEARCH_ENDPOINT}/locations/query"
        location_headers = {
            "apikey": API_FLIGHT_API_KEY
        }
        location_query = {
            "term": city_name,
            "locations": "city"
        }
        response = requests.get(url=location_endpoint, params=location_query, headers=location_headers)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def get_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        api_flight_header = {
            "apikey": API_FLIGHT_API_KEY
        }
        api_flight_query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "curr": "BRL"
        }

        response = requests.get(url=f"{API_FLIGHT_SEARCH_ENDPOINT}/v2/search",
                                params=api_flight_query, headers=api_flight_header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print("There is not flights for your query!")
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
        print(f"{flight_data.destination_city}: R${flight_data.price}")
        return flight_data

