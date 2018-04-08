#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api.accounts
    ~~~~~~~~~~~~~~~~~~~~

    This module implements the accounts API endpoints.
"""

from backend import restless
from backend.api import URL
from backend.models.account import Account


# ENDPOINT: /api/v1/accounts
restless.create_api(Account, methods          = ['GET', 'POST', 'DELETE', 'PUT'],
                             url_prefix       = URL,
                             collection_name  = 'accounts',
                             results_per_page = 0)