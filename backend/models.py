#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.models
    ~~~~~~~~~~~~~~

    This module implements the database models of this application.

    For more information on how to create models:
        - Flask-SQLAlchemy : http://flask-sqlalchemy.pocoo.org/2.3/
        - SQLAlchemy       : http://www.sqlalchemy.org/
"""

from datetime import datetime

from backend import db


# MODEL: User
class User(db.Model):
    """This is the user's model in the database."""
    __tablename__ = 'users'

    # Fields
    id              = db.Column(db.Integer, primary_key=True)
    email           = db.Column(db.String(50), nullable=False, unique=True)
    date_subscribed = db.Column(db.TIMESTAMP, nullable=False)

    # One-to-Many Relationship (1 User -> Many Accounts)
    accounts = db.relationship('Account', backref='users')

    def __init__(self, email):
        """
        This function initializes this model. 
        """
        self.email           = email
        self.date_subscribed = datetime.now()


# MODEL: Account
class Account(db.Model):
    """This is the account's model in the database."""
    __tablename__ = 'accounts'

    # Fields
    id           = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(50), nullable=False)
    details      = db.Column(db.String(50), nullable=False)
    user_id      = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)