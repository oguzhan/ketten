import datetime

from django.contrib.auth.models import User
from django.utils import unittest
from django.test.client import Client

from models import Chain


class ChainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user = User.objects.create_user('test', 'test@test.com', 'test')
        chain = {
            'id': 1,
            'title': 'Be cool',
            'starting_date': datetime.datetime.now(),
            'owner': user
        }
        chain = Chain(**chain)
        chain.save()

    def test_chain_details(self):
        client = Client()
        response = client.get('/chains/1/')
        self.assertEqual(response.status_code, 200)

    def test_chain_list(self):
        client = Client()
        response = client.get('/chains/')
        self.assertEqual(response.status_code, 200)
