import json
import unittest
from mock import Mock

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
        fake = '{ "age": 30, "city": "New York", "name": "John"}'
        mock_reponse.content = str(fake)
        mock_get.return_value = mock_reponse
        self.assertEqual({u'age': 30,  u'city': u'New York', u'name': u'John'}, self.base.getCountryInfo("egypt"))

    @patch('requests.get')
    def test_getCountryInfo_false(self, mock_get):
        mock_reponse = Mock()
        mock_reponse.status_code = 20

        mock_get.return_value = mock_reponse

        self.assertIsNone(self.base.getCountryInfo("egypt"))
