import requests
import unittest

class FlaskAppTests(unittest.TestCase):

    def test_get_request(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Request method: GET\nRequest data: None')

    def test_post_request(self):
        reponse = requests.post('http://localhost:5000', data='Hello, world!')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Request method: POST\nRequest data: Hello, world!')
        