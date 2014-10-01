import logging
from django import http


def home(request):
    logging.warning('warning')

    logging.error('error')

    logging.debug('debug')

    logging.info('info')

    logging.critical('critical')

    return http.HttpResponse('Hello World')
