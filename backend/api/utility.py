#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api.utility
    ~~~~~~~~~~~~~~~~~~~

    This module implements the utility API endpoints.
"""

from flask import request, make_response

from backend import app
from backend.api import URL


@app.route(URL + '/subscribe', methods=['POST'])
def subscribe():
    """
    Subscribes an user and sends an email.

    Request Example:
    POST
    {
        email : 'email address'
    }
    """
    data = request.get_json(force=True)
    print(data)
    # TODO: Data validation, subscribe user, and send email.
    return make_response('Works!', 201)