import urllib
from flask import Flask
from flask_testing import LiveServerTestCase

class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

    def test_getallengineers(self):
        response = urllib.request.urlopen(self.get_server_url()+"/getallengineers")
        self.assertEqual(response.code, 200)

    def test_eventsbyengineer(self):
        response = urllib.request.urlopen(self.get_server_url()+"/eventsbyengineer/sajan")
        self.assertEqual(response.code, 200)

    def test_events_valid(self):
        response = urllib.request.urlopen(self.get_server_url()+"/events?from=1509050542&to=1509050922")
        self.assertEqual(response.code, 200)

    def test_events_invalid1(self):
        response=0
        try:
            response = urllib.request.urlopen(self.get_server_url()+"/events?to=1509050922").getcode()
        except:
            self.assertNotEqual(response, 200)

    def test_summary(self):
        response = urllib.request.urlopen(self.get_server_url()+"/summary?date=1509115946")
        self.assertEqual(response.code, 200)

    def test_getallengineers_json(self):
        response = urllib.request.urlopen(self.get_server_url()+"/getallengineers")
        response_data=response.read().decode('utf-8')
        self.assertIsNotNone(response_data)

    def test_eventsbyengineer_json_value(self):
        response = urllib.request.urlopen(self.get_server_url()+"/eventsbyengineer/sajan")
        response_data = response.read().decode('utf-8')
        self.assertIsNotNone(response_data)

    def test_events_valid_json(self):
        response = urllib.request.urlopen(self.get_server_url()+"/events?from=1509050542&to=1509050922")
        response_data = response.read().decode('utf-8')
        self.assertIsNotNone(response_data)

    def test_summary_json(self):
        response = urllib.request.urlopen(self.get_server_url() + "/summary?date=1509115946")
        response_data = response.read().decode('utf-8')
        self.assertIsNotNone(response_data)

    def test_summary_json_value(self):
        response = urllib.request.urlopen(self.get_server_url()+"/summary?date=1509115946")
        response_data = response.read().decode('utf-8')
        self.assertIn("callista",response_data)

    def test_getallengineers_json_value(self):
        response = urllib.request.urlopen(self.get_server_url()+"/getallengineers")
        response_data=response.read().decode('utf-8')
        self.assertIn("isaac",response_data)

    def test_eventsbyengineer_json_value(self):
        response = urllib.request.urlopen(self.get_server_url()+"/eventsbyengineer/sajan")
        response_data = response.read().decode('utf-8')
        self.assertIn("15096384033449",response_data)

    def test_events_valid_json_value(self):
        response = urllib.request.urlopen(self.get_server_url()+"/events?from=1509050542&to=1509050922")
        response_data = response.read().decode('utf-8')
        self.assertIn("ines",response_data)