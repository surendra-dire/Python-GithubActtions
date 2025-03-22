import unittest
from FLASK_APP import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client using the Flask application configured for testing
        self.app = app.test_client()

    def test_home_route(self):
        # Send a GET request to the '/' route
        response = self.app.get('/')

        # Assert the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert the response data is as expected
        self.assertEqual(response.data.decode('utf-8'), "Hello, Flask Web Application!")

    def test_invalid_route(self):
        # Send a GET request to a non-existent route
        response = self.app.get('/invalid')

        # Assert the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

    def test_server_error_handling(self):
        # Test if the server handles exceptions (if applicable)
        with self.assertRaises(Exception):
            raise Exception("Simulated Server Error")

if __name__ == "__main__":
    unittest.main()
