import unittest
from unittest.mock import Mock

from api.data_access import get_stop_data, get_trip_data, get_stop_times_data


class TestDataAccess(unittest.TestCase):
    
    def test_get_stop_data(self):
        stop_id = "1"
        expected_result = {"stop_id": "1", "stop_name": "Stop 1"}
        mock_db = Mock()
        mock_db.stops.find_one.return_value = expected_result
        result = get_stop_data(mock_db, stop_id)
        self.assertEqual(result, expected_result)
        mock_db.stops.find_one.assert_called_once_with({"stop_id": stop_id})
    
    def test_get_trip_data(self):
        trip_id = "1"
        expected_result = {"trip_id": "1", "route_id": "1"}
        mock_db = Mock()
        mock_db.trips.find_one.return_value = expected_result
        result = get_trip_data(mock_db, trip_id)
        self.assertEqual(result, expected_result)
        mock_db.trips.find_one.assert_called_once_with({"trip_id": trip_id})
    
    def test_get_stop_times_data(self):
        trip_id = "1"
        expected_result = [
            {"stop_id": "1", "arrival_time": "01:00:00", "departure_time": "01:05:00"},
            {"stop_id": "2", "arrival_time": "01:20:00", "departure_time": "01:20:00"}
        ]
        mock_db = Mock()
        mock_db.stop_times.find.return_value = expected_result
        result = get_stop_times_data(mock_db, trip_id)
        self.assertEqual(result, expected_result)
        mock_db.stop_times.find.assert_called_once_with({"trip_id": trip_id})
