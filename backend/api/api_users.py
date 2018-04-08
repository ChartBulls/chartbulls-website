#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api.users
    ~~~~~~~~~~~~~~~~~

    This module implements the users API endpoints.
"""

from backend import restless
from backend.api import URL
from backend.models.user import User


# ENDPOINT: /api/v1/users
restless.create_api(User, methods          = ['GET', 'POST', 'DELETE', 'PUT'],
                          url_prefix       = URL,
                          collection_name  = 'users',
                          results_per_page = 0)