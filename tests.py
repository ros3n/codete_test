import json
import unittest
from mock import Mock
from werkzeug.test import Client
from wsgiservice import get_app
import guess_language
from controllers import LanguageDetector


class LanguageDetectorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = get_app(globals())
        self.client = Client(self.app)
        guess_language.guessLanguage = Mock(return_value='en')

    def test_post_request_with_valid_data(self):
        data = {'text': 'Hello world. Has the sun risen on you today.'}
        response, status, headers = self.client.post(data=data)

        self.assertEqual('200 OK', status)
        self.assertEqual({'language': 'en'}, json.loads(response[0]))
        self.assertIn('application/json', headers.get('Content-type'))

    def test_post_request_without_text(self):
        data = {}
        response, status, headers = self.client.post(data=data)

        self.assertEqual('200 OK', status)
        self.assertEqual({}, json.loads(response[0]))
        self.assertIn('application/json', headers.get('Content-type'))

    def test_get_request(self):
        response, status, headers = self.client.get()

        self.assertEqual('501 Not Implemented', status)

    def test_put_request(self):
        response, status, headers = self.client.put()

        self.assertEqual('501 Not Implemented', status)

    def test_delete_request(self):
        response, status, headers = self.client.delete()

        self.assertEqual('501 Not Implemented', status)


def run_tests():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(LanguageDetectorTestCase))
    runner = unittest.TextTestRunner()
    runner.run(test_suite)