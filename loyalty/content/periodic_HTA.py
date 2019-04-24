"""from __future__ import absolute_import, unicode_literals
from .HTA import *
from celery import shared_task

#PERIODIC FUNCTIONS
    #if using delay pushes new task for each reward to celery, else one big task. could be useful or not
    #calling the check fuction is one task, and wont complete until its done sending task to celery,
    #thus if not using delay could be increase the timing of the fuction tremdously. so its best send new tasks to celery

#run at morning, at time where server activity is at its least
@shared_task
def Periodic_Reward_Check_reward_after_purchase():
    rewards = Reward.objects.filter(criteria__applications='reward after purchase').filter(criteria__end_date=datetime.today()).filter(deactive_application=False)
    if rewards.exists():
        for i in rewards:
            reward_after_purchase.delay(reward_uuid=i.uuid, store_uuid=i.store.uuid, item_uuid=i.criteria.item_uuid, start_date=i.criteria.start_date, end_date=i.criteria.end_date)

@shared_task
def Periodic_Deal_Check_reward_after_purchase():
    deals = Deal.objects.filter(criteria__applications='reward after purchase').filter(criteria__end_date=datetime.today())
    if deal.exists():
        for i in deals:
            reward_after_purchase.delay(reward_uuid=i.uuid, store_uuid=i.store.uuid, item_uuid=i.criteria.item_uuid, start_date=i.criteria.start_date, end_date=i.criteria.end_date)

@shared_task
def Periodic_Reward_Check_special_day():
    rewards = Reward.objects.filter(criteria__applications='special day').filter(criteria__release_date=datetime.today())
    if rewards.exists():
        for i in rewards:
            special_day.delay(reward_uuid=i.uuid, store_uuid=i.store.uuid, release_date=i.criteria.release_date)

@shared_task
def Periodic_Deal_Check_special_day():
    deals = Deal.objects.filter(criteria__applications='special day').filter(criteria__release_date=datetime.today())
    if deals.exists():
        for i in deals:
            special_day.delay(reward_uuid=i.uuid, store_uuid=i.store.uuid, release_date=i.criteria.release_date)

@shared_task
def Periodic_Reward_Check_spent_amount_within_time():
    rewards = Reward.objects.filter(criteria__applications='spent_amount_within_time').filter(criteria__end_date=datetime.today())
    if rewards.exists():
        for i in rewards:
            spent_amount_within_time.delay(reward_uuid=i.uuid, store_uuid=i.store.uuid, amount=i.criteria.amount, start_date=i.criteria.start_date, end_date=i.criteria.end_date)

@shared_task
def Periodic_Deal_Check_spent_amount_within_time():
    deals = Deal.objects.filter(criteria__applications='spent_amount_within_time').filter(criteria__end_date=datetime.today())
    if deals.exists():
        for i in deals:
            spent_amount_within_time.delay(reward_uuid=i.uuid, store_uuid=i.store.uuid, amount=i.criteria.amount, start_date=i.criteria.start_date, end_date=i.criteria.end_date)

@shared_task
def Periodic_Reward_Check_birthday():
    rewards = Reward.objects.filter(criteria__applications='birthday').filter(deactive_application=False)
    if rewards.exists():
        for i in deals:
            birthday.delay(content_uuid=i.uuid, store_uuid=i.store.uuid, type='deal')

@shared_task
def Periodic_Deal_Check_birthday():
    deals = Deal.objects.filter(criteria__applications='birthday').filter(deactive_application=False)
    if deals.exists():
        for i in deals:
            birthday.delay(content_uuid=i.uuid, store_uuid=i.store.uuid, type='deal')

#run at night
@shared_task
def Periodic_Reward_Check_lifetime_total_spent_amount():
    rewards = Reward.objects.filter(criteria__applications='lifetime_total_spent_amount').filter(criteria__end_date=datetime.today()).filter(deactive_application=False)
    if rewards.exists():
        for i in rewards:
            lifetime_total_spent_amount.delay(content_uuid=i.uuid, store_uuid=i.store.uuid, item_uuid=i.criteria.item_uuid, start_date=i.criteria.start_date, end_date=i.criteria.end_date, type='reward')

@shared_task
def Periodic_Deal_Check_lifetime_total_spent_amount():
    deals = Deal.objects.filter(criteria__applications='lifetime_total_spent_amount').filter(criteria__end_date=datetime.today()).filter(deactive_application=False)
    if deals.exists():
        for i in deals:
            lifetime_total_spent_amount.delay(content_uuid=i.uuid, store_uuid=i.store.uuid, item_uuid=i.criteria.item_uuid, start_date=i.criteria.start_date, end_date=i.criteria.end_date, type='deal')
"""
