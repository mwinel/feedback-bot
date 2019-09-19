import json

from tests.base_test import BaseTestCase
from api.controllers.bot_controller import BotController


class TestBotEndpoints(BaseTestCase):

    def setUp(self):
        self.BaseSetUp()
        self.bot_controller = BotController(self.request_context)

    def test_bot(self):
        with self.app.app_context():
            response = self.client().post('/api/v1/bot/')

            response_json = json.loads(response.data.decode('utf-8'))
            self.assert200(response)
            self.assertEqual(response_json['text'], 'Welcome To Converge')
