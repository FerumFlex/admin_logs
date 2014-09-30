from admin_logs.log import get_record, set_record, RequestRecord


class LogRequestMiddleware(object):
    def process_request(self, request):
        record = RequestRecord(request)
        set_record(record)

    def process_response(self, request, response):
        record = get_record()
        if record:
            record.finish_request(response)
        return response
