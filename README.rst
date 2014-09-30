About
=====

This small module for django allows you to store requests in your database(now supports only database) and then loot at them in django admin. This module was inspired by logs in Google Application Engine


Configure
=========

Include this lines to your settings.py:


::

  INSTALLED_APPS += ('admin_logs', )
  MIDDLEWARE_CLASSES = ('admin_logs.middleware.LogRequestMiddleware', ) + MIDDLEWARE_CLASSES

  ADMIN_LOGS_BACKEND = 'admin_logs.backends.database.DatabaseBackend'

  from admin_logs import setup_level
  setup_level('INFO')


Working
=======

Anyway in the code you can run:

::

  import logging
  logging.warning('Test')


And this warning will be written to logs and you can check it later.