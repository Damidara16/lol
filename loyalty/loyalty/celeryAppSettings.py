CELERY_broker_url = 'pyamqp://'
#result_backend = 'rpc://'

CELERY_task_serializer = 'json'
#result_serializer = 'json'
CELERY_accept_content = ['json']
#timezone = 'Europe/Oslo'
CELERY_enable_utc = True

CELERY_task_routes = {
#    'tasks.add': 'low-priority',
}

CELERY_include = ['content.HTA','content.perodic_HTA']
