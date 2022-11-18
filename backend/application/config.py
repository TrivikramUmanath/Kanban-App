import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    SMTP_SERVER_HOST = "localhost"
    SMPTP_SERVER_PORT=1025
    SENDER_ADDRESS="vikram.umanath@gmail.com"
    SENDER_PASSWORD=""

class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory/db")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "testdb.sqlite3")
    DEBUG = True
    SECRET_KEY =  "secet"
    SECURITY_PASSWORD_HASH = "bcrypt"    
    SECURITY_PASSWORD_SALT = "secretive" # Read from ENV in your case
    SECURITY_REGISTERABLE = True
    SECURITY_CONFIRMABLE = False
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    WTF_CSRF_ENABLED = False
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    SMTP_SERVER_HOST = "localhost"
    SMPTP_SERVER_PORT=1025
    SENDER_ADDRESS="vikram.umanath@gmail.com"
    SENDER_PASSWORD=""


    # import os
# basedir = os.path.abspath(os.path.dirname(__file__))

# class Config():
#     DEBUG = False
#     SQLITE_DB_DIR = None
#     SQLALCHEMY_DATABASE_URI = None
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

# class LocalDevelopmentConfig(Config):
#     SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "db/testdb.sqlite3")
#     DEBUG = True