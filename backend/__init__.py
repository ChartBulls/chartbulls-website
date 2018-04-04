#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend package
    ~~~~~~~~~~~~~~~

    This is the main module of this application.

    Flask extensions included in this application:
    - Flask-SQLAlchemy : Used for creating database models (using SQLAlchemy).
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Creating the Flask app
app = Flask(__name__,
            template_folder='../frontend',
            static_folder='../frontend')
            
# Configuring the app from config module
app.config.from_pyfile('config.py')

# Initializing the Flask extensions
db = SQLAlchemy(app)

# Importing the database models
from backend import models

# Importing the app views
from backend import views