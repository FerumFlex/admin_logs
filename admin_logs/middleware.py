from admin_logs.log import get_record, set_record, RequestRecord

try:
    from django.utils.deprecation import MiddlewareMixin as parent
except ImportError:
    parent = object


class LogRequestMiddleware(parent):
    def process_request(self, request):
        record = RequestRecord(request)
        set_record(record)

    def process_response(self, request, response):
        record = get_record()
        if record:
            record.finish_request(response)
        return response
