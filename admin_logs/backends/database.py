# common
import uuid

# my
from admin_logs.models import Request


class DatabaseBackend(object):
    def save_record(self, record):
        request = Request(
            hash=uuid.uuid4(),
            start_date=record.start_date,
            duration=record.duration,
            url=record.url,
            status_code=record.status_code,
            ip=record.ip,
            content_length=record.content_length,
            user_agent=record.user_agent or "",
            entries=record.entries,
            max_level=record.max_level,
        )
        request.save()
