#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.models.user
    ~~~~~~~~~~~~~~~~~~~

    This module implements the user model.
"""

from datetime import datetime

from backend import db


class User(db.Model):
    __tablename__   = 'users'    
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(50), nullable=False, unique=True)
    date_subscribed = db.Column(db.TIMESTAMP, nullable=False)
    accounts        = db.relationship('Account', backref='users')

    def __init__(self, email):
        self.email           = email
        self.date_subscribed = datetime.now()