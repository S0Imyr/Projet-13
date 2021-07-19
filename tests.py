from django.test import Client


class Test:
    def setup_method(self):
        self.client = Client()

    def teardown_method(self):
        pass

    def test_index(self):
        pass
