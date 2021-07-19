from django.test import TestCase, Client


class Test:
    def setup_method(self):
        self.client = Client()

    def teardown_method(self):
        pass

    def test_profiles_index(self):
        pass

    def test_profiles(self):
        pass

