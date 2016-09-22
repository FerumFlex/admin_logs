import logging

from django.db import models

from picklefield.fields import PickledObjectField


class Request(models.Model):

    CT_NOT_SET = 0
    CT_PC = 1
    CT_MOBILE = 2
    CT_TABLET = 3
    CT_BOT = 4

    LEVEL_CHOICES = (
        (logging.CRITICAL, 'CRITICAL'),
        (logging.ERROR, 'ERROR'),
        (logging.WARNING, 'WARNING'),
        (logging.INFO, 'INFO'),
        (logging.INFO, 'INFO'),
        (logging.DEBUG, 'DEBUG'),
        (logging.NOTSET, 'NOTSET'),
    )

    hash = models.CharField(max_length=100, unique=True, editable=False,
                            verbose_name="Hash",
                            help_text="Unique identifier of request. "
                                      "Should be unique accross all requests.")

    start_date = models.DateTimeField(verbose_name="Request start time",
                                      editable=False, db_index=True)
    duration = models.FloatField(verbose_name="Duration in milleseconds",
                                 editable=False)
    max_level = models.SmallIntegerField(verbose_name="Max level",
                                         editable=False, db_index=True,
                                         default=logging.NOTSET,
                                         choices=LEVEL_CHOICES)

    url = models.CharField(max_length=1024, verbose_name="Request url",
                           editable=False, db_index=True)
    status_code = models.SmallIntegerField(verbose_name="Status code",
                                           editable=False, db_index=True)
    content_length = models.IntegerField(verbose_name="Content length",
                                         editable=False, null=True)
    user_agent = models.CharField(max_length=1024, editable=False, null=True)
    ip = models.GenericIPAddressField(editable=False, db_index=True)

    entries = PickledObjectField(default=[], editable=False)

    class Meta(object):
        ordering = ['-start_date']

    @property
    def milliseconds(self):
        return self.duration * 1000

    @property
    def formatted_start_date(self):
        return self.start_date.strftime('%Y-%m-%d %H:%M:%S') + '.' + \
            self.start_date.strftime('%f')[:3]

    @property
    def can_be_expanded(self):
        for entry in self.entries:
            if entry.stack_trace:
                return True
        return False
