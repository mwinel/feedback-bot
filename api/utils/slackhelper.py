import os
import slack
from decouple import config as env_config

SLACK_TOKEN = env_config('SLACK_TOKEN')


class Channel:

	def __init__(self, channel_info):
		self.id = channel_info["id"]
		self.name = channel_info["name"]
		self.members = channel_info["members"]


class SlackHelper:

	def __init__(self):
		self.slack_token = SLACK_TOKEN
		self.slack_client = slack.WebClient(SLACK_TOKEN, timeout=30)

	def get_channel_info(self):
		channel_object = self.slack_client.channels_info(
			channel="CNETSCVL7"
		)

		print(channel_object['channel']['members'])

		return ""
