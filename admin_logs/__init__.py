import logging

from admin_logs.log import AdminLogHandler


__version__ = (0, 1, '5')


default_app_config = 'admin_logs.apps.AdminLogsConfig'


handler = AdminLogHandler()
handler.setLevel(logging.DEBUG)
logging.root.addHandler(handler)
