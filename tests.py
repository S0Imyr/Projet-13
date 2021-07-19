from django.test import Client
from django.urls.base import reverse


class Test:
    def setup_method(self):
        self.client = Client()

    def teardown_method(self):
        pass

    def test_index(self):
        uri = reverse('index')
        response = self.client.get(uri)
        assert response.status_code == 200
