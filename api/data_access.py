# This file contains the code for accessing the GTFS data.

import pymongo

class DataAccess:
    def __init__(self, connection_string: str):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client["transit_db"]
        self.units = self.db["units"]
        self.routes = self.db["routes"]

    def get_unit_location(self, unit_id: int) -> Tuple[float, float]:
        # code to retrieve unit location from the database
        return lat, long

    def get_route_stops(self, route_id: int) -> List[str]:
        # code to retrieve route stops from the database
        return stops

    def save_unit_location(self, unit_id: int, lat: float, long: float):
        # code to save unit location to the database
        pass

    def save_route(self, route_id: int, name: str, stops: List[str]):
        # code to save route to the database
        pass
