#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.api.utility
    ~~~~~~~~~~~~~~~~~~~

    This module implements the utility API endpoints.
"""

from flask import request, make_response

from backend import app, db, mail
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

    found = User.query.filter_by(email=email).first()

    if found is None:
        # Add new user
        user = User(email)
        db.session.add(user)
        db.session.commit()
        # Send email
        msg = Message('Welcome to ChartBulls!', recipients=[email])
        msg.html = render_template('../backend/email_templates/subscribed.html')   
        mail.send(msg)
        # make response json object
        return make_response('Works!', 201)
    else:
        return make_response('Duplicate', 400)