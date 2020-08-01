#!/usr/bin python3

# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Python:
from unittest import TestCase
from urllib.parse import unquote
from tempfile import gettempdir
from os.path import join as path_join

# 3rd party:

# Internal: 
from uk_covid19 import Cov19API

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


test_filters = [
    'areaType=ltla',
    'areaName=adur'
]

test_structure = {
    "name": "areaName",
    "date": "date",
    "newCases": "newCasesBySpecimenDate"
}


class TestCov9Api(TestCase):
    def setUp(self) -> None:
        self.api = Cov19API(test_filters, test_structure)

    def test_options(self) -> None:
        data = Cov19API.options()

        self.assertIn("servers", data)

        server_url = data["servers"][0]["url"]
        self.assertEqual(Cov19API.endpoint, server_url)

    def test_api_params(self) -> None:
        from json import dumps

        api_params = {
            "filters": str.join(";", test_filters),
            "structure": dumps(test_structure, separators=(",", ":")),
        }

        self.assertDictEqual(self.api.api_params, api_params)

    def test_last_update(self):
        last_update = self.api.last_update

        # Ensure the timestamp is ISO-8601 compatible
        self.assertIn("Z", last_update)

    def test_head(self):
        location = (
            '/v1/data?'
            'filters=areaType=ltla;areaName=adur&'
            'structure={"name":"areaName","date":"date","newCases":"newCasesBySpecimenDate"}'
        )
        data = self.api.head()

        self.assertIn("Content-Location", data)
        self.assertEqual(location, unquote(data["Content-Location"]))

        self.assertIn("Last-Modified", data)

    def test_latest_by(self):
        api = Cov19API(test_filters, test_structure, latest_by="newCasesBySpecimenDate")

        # Test as dict object
        data = api.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn("data", data)
        self.assertIn("lastUpdate", data)
        self.assertIn("length", data)
        self.assertIn("totalPages", data)

        self.assertEqual(data["totalPages"], 1)
        self.assertEqual(len(data["data"]), 1)

        # Test keys
        for key in test_structure.keys():
            self.assertIn(key, data["data"][0])

    def test_get_json(self):
        from json import loads

        # Test as dict object
        data = self.api.get_json()
        self.assertIsInstance(data, dict)
        self.assertIn("data", data)
        self.assertIn("lastUpdate", data)
        self.assertIn("length", data)
        self.assertIn("totalPages", data)

        self.assertGreaterEqual(data["totalPages"], 1)
        self.assertGreater(len(data["data"]), 10)

        # Test keys
        for key in test_structure.keys():
            self.assertIn(key, data["data"][0])

        # Test as str object
        data_str = self.api.get_json(as_string=True)
        self.assertIsInstance(data_str, str)

        json_dict = loads(data_str)
        self.assertDictEqual(json_dict, data)

        # Test as file object
        temp_dir = gettempdir()
        temp_path = path_join(temp_dir, "data.json")
        self.api.get_json(save_as=temp_path)

        with open(temp_path, "r") as pointer:
            file_data = pointer.read().strip()

        self.assertEqual(data_str, file_data)

    def test_get_xml(self):
        from xml.etree.ElementTree import Element

        # Test as xml object
        data = self.api.get_xml()
        self.assertIsInstance(data, Element)
        self.assertGreater(len(data.findall(".//data")), 10)
        self.assertIsInstance(data.find(".//lastUpdate").text, str)
        self.assertIsInstance(data.find(".//length").text, str)
        self.assertIsInstance(data.find(".//totalPages").text, str)

        self.assertGreater(int(data.find(".//length").text), 10)
        self.assertGreaterEqual(int(data.find(".//totalPages").text), 1)

        # Test keys
        for key in test_structure.keys():
            self.assertEqual(data.find(f".//data/{key}").tag, key)

        # Test as str object
        data_str = self.api.get_xml(as_string=True)
        self.assertIsInstance(data_str, str)

        # Test as file object
        temp_dir = gettempdir()
        temp_path = path_join(temp_dir, "data.xml")
        self.api.get_xml(save_as=temp_path)

        with open(temp_path, "r") as pointer:
            file_data = pointer.read().strip()

        self.assertEqual(data_str, file_data)

    def test_get_csv(self):
        data = self.api.get_csv()
        self.assertIsInstance(data, str)
        self.assertGreater(len(data.split()), 10)

        # Test keys
        self.assertEqual(data.split()[0], str.join(",", test_structure.keys()))

        # Test as file object
        temp_dir = gettempdir()
        temp_path = path_join(temp_dir, "data.csv")
        self.api.get_csv(save_as=temp_path)

        with open(temp_path, "r") as pointer:
            file_data = pointer.read().strip()

        self.assertEqual(data.strip(), file_data)