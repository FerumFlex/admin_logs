import logging

from admin_logs.log import AdminLogHandler


__version__ = (0, 1, '2')


def setup_level(level):
    handler = AdminLogHandler()
    handler.setLevel(level)
    logging.root.addHandler(handler)
