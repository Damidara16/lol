CELERY_broker_url = 'amqp://localhost//'
#result_backend = 'rpc://'

#CELERY_task_serializer = 'json'
#result_serializer = 'json'
CELERY_accept_content = ['json']
#timezone = 'Europe/Oslo'
CELERY_enable_utc = True

CELERY_task_routes = {
#    'tasks.add': 'low-priority',
}

#CELERY_include = ['content.HTA','content.perodic_HTA']

"""
CELERY_BEAT_SCHEDULE = {
    # Executes every Friday at 4pm
    'send-notification-on-friday-afternoon': {
         'task': 'loyalty.periodic_HTA.Periodic_Deal_Check_special_day',
         'schedule': crontab(hour=16, day_of_week=5),
        },
}
"""
