from os import environ


class Config:
    ######################### Application Config #########################
    ENV = environ.get("RCDAT_AUTHZ_ENV", "production")
    DEBUG = bool(int(environ.get("RCDAT_AUTHZ_DEBUG", "0")))
    TESTING = bool(int(environ.get("RCDAT_AUTHZ_TESTING", "0")))
    SECRET_KEY = environ.get("RCDAT_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
    TIMEZONE = environ.get("RCDAT_AUTHZ_TIMEZONE", "Asia/Tehran")
    ########################## Database Config ###########################
    SQLALCHEMY_DATABASE_URI = environ.get("RCDAT_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    ############################# User Config #############################
    USER_DEFAULT_ROLE = environ.get("RCDAT_AUTHZ_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_EXPIRY_TIME = int(environ.get("RCDAT_AUTHZ_USER_DEFAULT_EXPIRY_TIME", "365"))
    USER_DEFAULT_STATUS = int(environ.get("RCDAT_AUTHZ_USER_DEFAULT_STATUS", "3"))

