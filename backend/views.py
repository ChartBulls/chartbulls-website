#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.views
    ~~~~~~~~~~~~~

    This module implements the views of this application.
"""

from flask import render_template

from backend import app


@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def index(path):
    """
    Serves the index page of this application.
    """
    return render_template('index.html')