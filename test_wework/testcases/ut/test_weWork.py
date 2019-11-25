from unittest import TestCase

from test_wework.api.wework import WeWork


class TestWeWork(TestCase):
    def test_get_token(self):
        wework = WeWork()
        token = wework.get_access_token()
        assert token != None
