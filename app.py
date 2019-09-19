from decouple import config as env_config
from api import create_app
from flask_script import Manager

app = create_app(env_config('ENV'))
manager = Manager(app)

@manager.command
def run_server():
    app.run(
        env_config('HOST'),
        port=5500,
        debug=True
    )

if __name__ == "__main__":
    manager.run()
