import time
import logging
import traceback
import threading
import importlib

from django.utils import timezone
from django.conf import settings, ImproperlyConfigured


_thread_locals = threading.local()


def get_record():
    return _thread_locals.record if hasattr(_thread_locals, 'record') else None


def set_record(record):
    _thread_locals.record = record


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip_address = x_forwarded_for.split(',')[0]
    else:
        ip_address = request.META.get('REMOTE_ADDR')
    return ip_address or ''


def load_backend(path):
    i = path.rfind('.')
    module, attr = path[:i], path[i + 1:]
    try:
        mod = importlib.import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing '
                                   'admin log backend %s: "%s"' % (path, e))
    except ValueError:
        raise ImproperlyConfigured('Error importing admin log backends. '
                                   'Is ADMIN_LOGS_BACKEND a correctly'
                                   ' defined list or tuple?')
    try:
        cls = getattr(mod, attr)
    except AttributeError:
        raise ImproperlyConfigured('Module "%s" does not define a '
                                   '"%s" admin logs backend' % (module, attr))
    return cls()


class RequestRecordEntry(object):
    def __init__(self):
        self.time = time.time()
        self.message = None
        self.level = 0
        self.stack_trace = None

    def formatted_date(self):
        date = timezone.datetime.fromtimestamp(self.time)
        date_format = '%Y-%m-%d %H:%M:%S'
        return date.strftime(date_format) + '.' + date.strftime('%f')[:3]

    def formatted_level(self):
        return str(logging.getLevelName(self.level))[:1].lower()


class RequestRecord(object):
    def __init__(self, request):
        self.start_date = timezone.now()
        self.duration = 0
        self.start_request = time.time()
        self.url = (request.path or '')[:1024]
        self.status_code = None
        self.ip = get_client_ip(request)[:39]
        self.content_length = 0
        self.user_agent = request.META.get('HTTP_USER_AGENT', '')[:1024]
        self.entries = []
        self.max_level = 0

    def finish_request(self, response):
        self.status_code = response.status_code
        self.duration = time.time() - self.start_request
        self.content_length = len(response.content) if hasattr(response, 'content') else 0

        self.save_backend()

    def add_entry(self, record):
        message = record.getMessage()

        entry = RequestRecordEntry()
        entry.message = message
        entry.level = record.levelno
        if record.exc_info:
            entry.stack_trace = traceback.format_exception(*record.exc_info)
            entry.stack_trace = '\n'.join(entry.stack_trace)

        self.max_level = max(self.max_level, record.levelno)
        self.entries.append(entry)

    def save_backend(self):
        backend = load_backend(settings.ADMIN_LOGS_BACKEND)
        backend.save_record(self)


class AdminLogHandler(logging.Handler):

    def handle(self, record):
        self.acquire()
        try:
            self.emit(record)
        finally:
            self.release()
        return 1

    def emit(self, record):
        request = get_record()
        if not request:
            return

        request.add_entry(record)
