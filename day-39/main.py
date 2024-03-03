from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

datamanager = DataManager()
sheet_data = datamanager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "SAO"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_code(row["city"])
    datamanager.destination_data = sheet_data
    datamanager.update_destination_data()

tomorrow = datetime.now() + timedelta(days=1)
return_date = datetime.now() + timedelta(days=(6))

for destination in sheet_data:
    flight = flight_search.get_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=return_date
    )
    if flight.price < destination["lowestPrice"]:
        print("Notification system...")
