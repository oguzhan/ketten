from django.utils import unittest
from django.test.client import Client


class ChainTest(unittest.TestCase):
    def test_chain_details(self):
        client = Client()
        response = client.get('/chains/1')
        self.assertEqual(response.status_code, 200)

    def test_chain_list(self):
        client = Client()
        response = client.get('/chains/')
        self.assertEqual(response.status_code, 200)
