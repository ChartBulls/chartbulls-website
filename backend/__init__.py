#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend package
    ~~~~~~~~~~~~~~~

    This is the main module of this application.
"""

from flask import Flask


# Creating the Flask app
app = Flask(__name__,
            template_folder='../frontend',
            static_folder='../frontend')
            
# Configuring the app from config module
app.config.from_pyfile('config.py')

# Importing the app views
from backend import views