from flask_testing import TestCase
import json
from app import create_app

class BaseTestCase(TestCase):

	def BaseSetUp(self):
		"""initialize app"""
		self.app = self.create_app()
		self.client = self.app.test_client

	def create_app(self):
		"""Create the app and specify 'testing' as the environment"""
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		self.client = self.app.test_client()
		self.request_context = self.app.test_request_context()

		return self.app
