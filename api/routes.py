# This file contains the API endpoints and their corresponding functions.

class Route:
    def __init__(self, route_id: int, name: str, stops: List[str]):
        self.route_id = route_id
        self.name = name
        self.stops = stops
