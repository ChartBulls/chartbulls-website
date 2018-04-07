#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.commands
    ~~~~~~~~~~~~~~~~
    
    This module implements the CLI commands of this application.

    Commands:
    - run      : Runs the application (host: localhost, port: 5000).
    - create   : Creates all of the tables in the database.
    - drop     : Drops all of the tables from the database.
    - recreate : Drops and recreates the tables in the database.
    - db       : Performs database migrations.

    HOW TO USE:
    - Type the following in the command-line:
      flask [COMMAND]
"""

import click

from backend import app, db


# COMMAND: create
@app.cli.command()
def create():
    """Creates all of the tables in the database."""
    db.create_all()
    click.echo('Created all of the tables in the database.')


# COMMAND: drop
@app.cli.command()
def drop():
    """Drops all of the tables from the database."""
    db.drop_all()
    click.echo('Dropped all of the tables from the database.')


# COMMAND: recreate
@app.cli.command()
def recreate():
    """Drops and recreates the tables in the database."""
    db.drop_all()
    db.create_all()
    click.echo('Recreated all of the tables in the database.')