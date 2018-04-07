#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.models.account
    ~~~~~~~~~~~~~~~~~~~~~~

    This module implements the account model.
"""

from backend import db


class Account(db.Model):
    __tablename__ = 'accounts'    
    id            = db.Column(db.Integer, primary_key=True)
    account_type  = db.Column(db.String(50), nullable=False)
    details       = db.Column(db.String(50), nullable=False)
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)