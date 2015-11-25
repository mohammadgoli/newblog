import os 
from datetime import timedelta

#first we initialize the current folder
basedir = os.path.abspath(os.path.dirname(__file__))

#second we define the database name 
DATABASE_NAME = 'blog.db'

#the user name and password for me (admin :P)
USERNAME = 'admin22'
PASSWORD = '12345'

#3rd we combine the things to define database path 
DATABASE_PATH = os.path.join(basedir, DATABASE_NAME)

#SQLi database path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH

# otherConfigs
CSRF_ENABLED = True
SECRET_KEY = os.urandom(24)

#for recaptcha
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_PARAMETERS = {'hl': 'fa'}

PERMANENT_SESSION_LIFETIME = timedelta(days=3)

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'gli.mhmd@gmail.com'
MAIL_PASSWORD = 'sheE111@!'
DEFAULT_MAIL_SENDER = 'gli.mhmd@gmail.com'