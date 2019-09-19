from flask_api import FlaskAPI
from flask_cors import CORS
from api.blueprints.base_blueprint import BaseBlueprint
from flask_mongoengine import MongoEngine


def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=False)
    app.config.from_object('config.config.Config')
    db = MongoEngine(app)


    # CORS
    CORS(app)

    # Blueprints
    blueprint = BaseBlueprint(app)
    blueprint.register()

    return app
