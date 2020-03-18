import json
import unittest
from unittest.mock import Mock

from mock import patch

from baseApi import baseApi


class baseApi_test(unittest.TestCase):

    def setUp(self):
        self.base = baseApi()

    @patch('requests.get')
    def test_connection_true(self, mock_get):
        mock_reponse = Mock()
        mock_reponse.status_code = 200

        mock_get.return_value = mock_reponse

        self.assertEqual(True, self.base.connection())

    @patch('requests.get')
    def test_connection_false(self, mock_get):
        mock_reponse = Mock()
        mock_reponse.status_code = 20

        mock_get.return_value = mock_reponse

        self.assertEqual(False, self.base.connection())

    @patch('requests.get')
    def test_getCountryInfo_true(self, mock_get):
        mock_reponse = Mock()
        mock_reponse.status_code = 200
        fake = '{ "name":"John", "age":30, "city":"New York"}'
        mock_reponse.content = fake
        mock_get.return_value = mock_reponse

        self.assertEqual(str({'name': 'John', 'age': 30, 'city': 'New York'}), str(self.base.getCountryInfo("egypt")))

    @patch('requests.get')
    def test_getCountryInfo_false(self, mock_get):
        mock_reponse = Mock()
        mock_reponse.status_code = 20

        mock_get.return_value = mock_reponse

        self.assertIsNone(self.base.getCountryInfo("egypt"))
