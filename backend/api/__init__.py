#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api package
    ~~~~~~~~~~~~~~~~~~~

    This package contains the API endpoints of this application.

    For more information on how to create the API endpoints:
        - Flask-Restless : https://flask-restless.readthedocs.io/en/stable/
"""

# URL for the API version
URL = '/api/v1'

from backend.api import api_users
from backend.api import api_accounts