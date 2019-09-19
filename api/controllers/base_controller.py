import json
import requests
from flask import jsonify, make_response, request
from api.utils.slack_blocks import (
	taking_feedback_message,
	thank_you_message,
	cancellation_message
)


class BaseController:

	def __init__(self, request):
		self.request = request

	def handle_response(self, msg='OK', payload=None, status_code=200, slack_response=None):

		# If there is no specific slack formatted response, default to WEB API Response format
		if slack_response is None:
			data = {'msg': msg}
			if payload is not None:
				data['payload'] = payload
		else:
			data = slack_response

		response = jsonify(data)
		response.status_code = status_code
		return response

	def send_taking_feedback_message(self, url):
		""" POST response on dialog form trigger. """
		messsage = taking_feedback_message
		return requests.post(url, data=json.dumps(messsage))

	def send_thankyou_message(self, url):
		""" POST response on dialog submission. """
		message = thank_you_message
		return requests.post(url, data=json.dumps(message))

	def cancel_feedback_submission(self, url):
		""" POST response on cancel dialog submission trigger. """ 
		message = cancellation_message
		return requests.post(url, data=json.dumps(message))
