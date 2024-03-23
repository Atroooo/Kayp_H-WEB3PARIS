from django.test import TestCase, Client
from django.urls import reverse


def test_manageContract_GET(self):
    client = Client()
    response = client.get(reverse('manageContract'))

    self.assertEqual(response.status_code, 200)