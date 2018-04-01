#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend package
    ~~~~~~~~~~~~~~~

    This is the main module of this application.
"""

from flask import Flask


app = Flask(__name__)
            
# Configuring the app from config module
app.config.from_pyfile('config.py')

@app.route("/")
def hello():
    return "<h1>Test</h1>"