About
=====

This small module for django allows you to store requests in your database(now supports only database) and then look at them in django admin.
This module was inspired by logs in Google Application Engine


Configure
=========

Include this lines to your settings.py:


::

  INSTALLED_APPS += ('admin_logs', )
  MIDDLEWARE_CLASSES = ('admin_logs.middleware.LogRequestMiddleware', ) + MIDDLEWARE_CLASSES  # place middleware as early as possible

  ADMIN_LOGS_BACKEND = 'admin_logs.backends.database.DatabaseBackend'  # now supports only database

  from admin_logs import setup_level
  setup_level('INFO')  # set minumum log level that will be written to logs

And this warning will be written to logs and you can check it later.