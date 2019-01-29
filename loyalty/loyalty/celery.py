from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from content.periodic_HTA import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loyalty.settings')

app = Celery('loyalty')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_period_task(crontab(hour=5,minute=0, day_of_week="*"), Periodic_Reward_Check_reward_after_purchase.s())
    sender.add_period_task(crontab(hour=5,minute=15, day_of_week="*"), Periodic_Reward_Check_special_day.s())
    sender.add_period_task(crontab(hour=5,minute=25, day_of_week="*"), Periodic_Reward_Check_spent_amount_within_time.s())
    sender.add_period_task(crontab(hour=5,minute=30, day_of_week="*"), Periodic_Reward_Check_birthday.s())
    sender.add_period_task(crontab(hour=18,minute=0, day_of_week="*"), Periodic_Reward_Check_lifetime_total_spent_amount.s())

    sender.add_period_task(crontab(hour=5,minute=5, day_of_week="*"), Periodic_Deal_Check_reward_after_purchase.s())
    sender.add_period_task(crontab(hour=5,minute=10, day_of_week="*"), Periodic_Deal_Check_special_day.s())
    sender.add_period_task(crontab(hour=5,minute=20, day_of_week="*"), Periodic_Deal_Check_spent_amount_within_time.s())
    sender.add_period_task(crontab(hour=5,minute=35, day_of_week="*"), Periodic_Deal_Check_birthday.s())
    sender.add_period_task(crontab(hour=18,minute=10, day_of_week="*"), Periodic_Deal_Check_lifetime_total_spent_amount.s())

app.config_from_object('loyalty.celeryAppSettings', namespace= 'CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
