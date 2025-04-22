"""
Separating application settings from the rest of the application
"""

import os

# set up path of the database file
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    
    """
    Set configuration values 
    """
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # disable tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False