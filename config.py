import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Set track mods to off to suppress over head
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Connect to the database

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgres://jiayiguo@localhost:5432/Fyyur'