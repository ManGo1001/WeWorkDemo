from unittest import TestCase

import requests

from test_wework.utils.util import Utils


class TestUtils(TestCase):
    def test_format(self):
        print(Utils.format({"a": 1, "b": {"c": "xxx"}}))

    def test_format1(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        print(Utils.format(r))

    def test_jsonpath(self):
        r = requests.get("https://testerhome.com/api/v3/topics.json?limit=2").json()
        print(Utils.format(r))
        assert Utils.jsonpath(r, "$..topics[?(@.excellent == 0)]")[0]["id"]>10000




