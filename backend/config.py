#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.config
    ~~~~~~~~~~~~~~

    This module contains the configuration values of this application.

    For more information on how to handle configuration
    - Flask : http://flask.pocoo.org/docs/0.12/config/
"""

import os


# Flask configuration values
DEBUG = os.environ.get('DEBUG', True)