import unittest
from unittest.mock import Mock, patch

from api.routes import app


class TestRoutes(unittest.TestCase):
    
    def setUp(self):
        self.client = app.test_client()

    def test_get_stops(self):
        expected_result = {
            "stops": [
                {"stop_id": "1", "stop_name": "Stop 1"},
                {"stop_id": "2", "stop_name": "Stop 2"}
            ]
        }
        response = self.client.get('/stops')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
    
    @patch('api.routes.get_stop_data')
    def test_get_stop_by_id(self, mock_get_stop_data):
        mock_stop = {"stop_id": "1", "stop_name": "Stop 1"}
        mock_get_stop_data.return_value = mock_stop
        expected_result = mock_stop
        response = self.client.get('/stops/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_result)
    
    def test_invalid_stop_id(self):
        response = self.client.get('/stops/invalid')
        self.assertEqual(response.status_code, 400)
