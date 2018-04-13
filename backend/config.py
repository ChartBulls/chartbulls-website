#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.config
    ~~~~~~~~~~~~~~

    This module contains the configuration values of this application.

    For more information on how to handle configuration:
    - Flask            : http://flask.pocoo.org/docs/0.12/config/
    - Flask-Mail       : https://pythonhosted.org/Flask-Mail/
    - Flask-SQLAlchemy : http://flask-sqlalchemy.pocoo.org/2.3/config/
"""

import os


# Flask
DEBUG = os.environ.get('DEBUG', True)

# Flask-Mail
MAIL_SERVER         = os.environ.get('MAIL_SERVER', 'localhost')
MAIL_PORT           = os.environ.get('MAIL_PORT', 25)
MAIL_DEBUG          = os.environ.get('MAIL_DEBUG', 1)
MAIL_USE_SSL        = os.environ.get('MAIL_USE_SSL', False)
MAIL_USERNAME       = os.environ.get('MAIL_USERNAME', 'email@address.com')
MAIL_PASSWORD       = os.environ.get('MAIL_PASSWORD' 'password')
MAIL_DEFAULT_SENDER = ('ChartBulls', MAIL_USERNAME)

# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI        = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost:5432/app_db')
SQLALCHEMY_TRACK_MODIFICATIONS = False