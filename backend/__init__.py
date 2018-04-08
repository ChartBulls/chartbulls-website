#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend package
    ~~~~~~~~~~~~~~~

    This is the main module of this application.

    Flask extensions included in this application:
    - Flask-SQLAlchemy : Used for creating database models (using SQLAlchemy).
    - Flask-Migrate    : Used for performing SQLAlchemy database migrations.
    - Flask-Restless   : Used for creating the REST API.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate


# Creating the Flask app
app = Flask(__name__,
            template_folder='../frontend',
            static_folder='../frontend')
            
# Configuring the app from config module
app.config.from_pyfile('config.py')

# Initializing the Flask extensions
db       = SQLAlchemy(app)
restless = APIManager(app, flask_sqlalchemy_db=db)
migrate  = Migrate(app, db)

# Importing the database models
from backend import models

# Importing the API endpoints
from backend import api

# Importing the app views
from backend import views

# Importing the CLI commands
from backend import commands