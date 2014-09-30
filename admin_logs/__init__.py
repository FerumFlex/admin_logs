import logging

from admin_logs.log import AdminLogHandler


def setup_level(level):
    handler = AdminLogHandler()
    handler.setLevel(level)
    logging.root.addHandler(handler)
