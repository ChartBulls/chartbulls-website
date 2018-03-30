#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend package
    ~~~~~~~~~~~~~~~

    This is the main module of this application.
"""

from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Test</h1>"