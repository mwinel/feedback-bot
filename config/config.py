from decouple import config as env_config

class Config(object):
    ENV = env_config('ENV', default='development')
    DEBUG = env_config('DEBUG', default=False, cast=bool)
