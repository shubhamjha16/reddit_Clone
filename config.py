import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Configuration settings for the Flask application
# Add your configurations here
# For example:
# SECRET_KEY = 'your_secret_key'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
