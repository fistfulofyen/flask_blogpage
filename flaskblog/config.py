import os

class Config:
    # hide info in envirment varable
    '''
    For Windows:
    control panel > system and security > systems > advanced system settings > envirment variable

    user varable will do

    new >> variable name = '...', variable value = '...'

    environ is a dict

    see email section

    not using now cus sqlite
    '''
    SECRET_KEY = '0e9060de7de2f0f916ba4703d7af69be'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'stmp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')