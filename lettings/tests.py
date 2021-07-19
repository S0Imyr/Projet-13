from django.test import Client
from django.urls.base import reverse

import pytest

from .models import Address, Letting


class Test:
    def setup_method(self):
        self.client = Client()
        self.address = Address.objects.create(number=555, street='Test street', city="Test City", state="Test State", zip_code=92000, country_iso_code='AX')
        self.letting = Letting.objects.create(title="Test title", address=self.address)

    def teardown_method(self):
        Address.objects.all().delete()
        Letting.objects.all().delete()

    @pytest.mark.django_db
    def test_letting_index(self):
        uri = reverse('lettings_index')
        response = self.client.get(uri)
        assert response.status_code == 200
    
    @pytest.mark.django_db
    def test_letting(self):
        letting_id = 1
        uri = reverse('letting', args=[letting_id])
        response = self.client.get(uri)
        assert response.status_code == 200
