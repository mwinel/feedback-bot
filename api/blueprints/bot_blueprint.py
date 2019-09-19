from api.blueprints.base_blueprint import Blueprint, BaseBlueprint, request
from api.controllers.bot_controller import BotController

url_prefix = '{}/bot'.format(BaseBlueprint.base_url_prefix)
bot_blueprint = Blueprint('bot', __name__, url_prefix=url_prefix)
bot_controller = BotController(request)


@bot_blueprint.route('/', methods=['GET', 'POST'])
def welcome_message():
	""" API endpoint to display welcome block. """
	return bot_controller.parse_welcome_block()

@bot_blueprint.route('/feedback-form', methods=['GET', 'POST'])
def feedback_form():
	""" API endpoint to display feedback form. """
	return bot_controller.parse_feedback_actions()
