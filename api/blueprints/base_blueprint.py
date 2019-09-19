from flask import Blueprint, request

class BaseBlueprint:

	base_url_prefix = '/api/v1'

	def __init__(self, app):
		self.app = app

	def register(self):
		''' Register All App Blue Prints Here '''
    
		from api.blueprints.bot_blueprint import bot_blueprint

		self.app.register_blueprint(bot_blueprint)
