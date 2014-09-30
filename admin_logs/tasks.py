# common
import datetime

# django
from django.utils import timezone

# other
from celery.schedules import crontab
from celery.task import periodic_task, group, task

# my
from admin_logs.models import Request


def process_models_with_chunks(task, iterable, count_per_chunk,
                               delta_countdown=None):
    def model_chunker(iterable, count_per_chunk):
        results_ids = []

        for obj in iterable.only('id'):
            if len(results_ids) == count_per_chunk:
                yield results_ids
                results_ids = []

            results_ids.append(obj.id)

        if results_ids:
            yield results_ids

    count = 0
    tasks = []
    for model_ids in model_chunker(iterable, count_per_chunk):
        options = None
        if delta_countdown:
            options = {
                'countdown': delta_countdown * count,
            }
        t = task.subtask((model_ids, iterable.model), options=options)
        tasks.append(t)
        count += 1

    return group(*tasks).apply_async()


@periodic_task(run_every=crontab(minute="0", hour="2"), ignore_result=True)
def clean_requests():
    start_date = timezone.now() - datetime.timedelta(days=30)
    query = Request.objects.filter(start_date__lte=start_date)
    return process_models_with_chunks(clean_requests_chunk, query, 10)


@task(ignore_result=True)
def clean_requests_chunk(request_ids, class_class):
    query = class_class.objects.filter(id__in=request_ids)
    for req in query:
        req.delete()