import logging
from django import http


def home(request):
    logging.warning('warning')

    logging.error('error')

    try:
        t = {}
        t['id']
    except:
        logging.exception('error with traceback')

    logging.debug('debug')

    logging.info('info')

    logging.critical('critical')

    try:
        1 / 0
    except:
        logging.exception('error with traceback')

    return http.HttpResponse('Hello World')
