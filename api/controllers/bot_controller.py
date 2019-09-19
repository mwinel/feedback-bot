import os
import json
import requests
from flask import make_response, request
from api.utils.slackhelper import SlackHelper
from api.utils.slack_blocks import (
    hello_message,
    welcome_attachment,
    feedback_form
)
from api.controllers.base_controller import BaseController


SLACK_VERIFICATION_TOKEN = os.environ["SLACK_VERIFICATION_TOKEN"]

def verify_slack_token(request_token):
    """
    Helper function to verify incoming slack requests.

    :Arguments:
    - request_token: slack verification token.

    :Returns:
    - 403 response if veirication token is invalid
    """
    if SLACK_VERIFICATION_TOKEN != request_token:
        return make_response("Invalid slack verification token.", 403)


class BotController(BaseController):
    def __init__(self, request):
        BaseController.__init__(self, request)
        self.slackhelper = SlackHelper()

        import pprint

        channel_object = self.slackhelper.get_channel_info()
        pprint.pprint(channel_object)
     
    def parse_welcome_block(self):
        """
        Post a message containing a set of buttons to begin
        the feedback workflow.

        :Arguments:
        - None

        :Returns:
        - slack block
        """
        
        return self.handle_response(slack_response={
            "as_user": False,
            "channel": os.environ["SLACK_CHANNEL"],
            "text": hello_message,
            "attachments": json.dumps(welcome_attachment)
        })

    def parse_feedback_actions(self):
        """
        Trigger slack actions and display form elements.

        :Arguments:
        - None

        :Returns:
        - feedback form
        """

        # Parse request payload
        form_json = json.loads(request.form["payload"])
        # Retrieve response url
        url = form_json["response_url"]
        # Verify that requests are coming from slack
        verify_slack_token(form_json["token"])
        if form_json["type"] == "interactive_message":
            self.slackhelper.slack_client.dialog_open(
                as_user=False,
                trigger_id=form_json["trigger_id"],
                dialog=feedback_form
            )
            self.send_taking_feedback_message(url)
        elif form_json["type"] == "dialog_submission":
            self.send_thankyou_message(url)

        # Add response on submission cancellation

        return make_response("", 200)
