from os import environ


class Config:
    ENV = environ.get("RCDAT_AUTHZ_ENV", "production")
    DEBUG = bool(int(environ.get("RCDAT_AUTHZ_DEBUG", "0")))
    TESTING = bool(int(environ.get("RCDAT_AUTHZ_TESTING", "0")))
    SECRET_KEY = environ.get("RCDAT_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
