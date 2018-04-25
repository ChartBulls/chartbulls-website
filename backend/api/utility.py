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
from backend.models.user import User


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
    data      = request.get_json(force=True)
    email     = data.get('email', None)
    criterion = [email, len(data) == 1]

    if not all(criterion):
        return make_response('Bad Request', 400)

    user = User.query.filter_by(email=email).first()

    if user is None:
        # add user

        # send email

        return make_response('Works!', 302)
    else:
        return make_response('Duplicate', 400)