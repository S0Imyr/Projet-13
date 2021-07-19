from django.test import Client
from django.urls.base import reverse

import pytest

from .models import User, Profile


class Test:
    def setup_method(self):
        self.client = Client()
        self.user = User.objects.create(username="test_user")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Charleville Mézières")

    def teardown_method(self):
        pass

    @pytest.mark.django_db
    def test_profiles_index(self):
        uri = reverse('profiles_index')
        response = self.client.get(uri)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_profiles(self):
        uri = reverse('profile', args=[self.profile.user.username])
        response = self.client.get(uri)
        assert response.status_code == 200
