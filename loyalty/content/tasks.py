#from __future__ import absolute_import, unicode_literals
#from content.models import Reward, Deal
from django.db.models import Sum
from celery import Celery
from celery import shared_task

@shared_task
def addNewUserContent(uuid, customer_uuid, reward=True):
    if reward == False:
        d = Deal.objects.get(uuid=uuid)
        cu = Customer.objects.get(uuid=customer_uuid)
        cu.deals.add(d)
    else:
        r = Reward.objects.get(uuid=uuid)
        cu = Customer.objects.get(uuid=customer_uuid)
        cu.rewards.add(r)

"""
ADD TRY STATEMENTS TO ADD FUNCTIONS INCASE STORE DELETES REWARD
"""
#LONG RUNNING/AWAITED APPLICATION REWARDS
@shared_task
def birthday(content_uuid, store_uuid, type):
    if type == 'reward':
        try:
            reward = Reward.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            qs = store.customers.filter(birthday=datetime.today())
            if qs.exists():
                for i in qs:
                    i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
    elif type == 'deal':
        try:
            deal = Deal.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            qs = store.customers.filter(birthday=datetime.today())
            if qs.exists():
                for i in qs:
                    i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
    #qs = store.customers.objects.filter()
@shared_task
def lifetime_total_spent_amount(content_uuid, store_uuid, amount, type):
    if type == 'reward':
        try:
            reward = Reward.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            qs = store.customers.filter(total__gt=amount)
            if qs.exists():
                for i in qs:
                    i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
    elif type == 'deal':
        try:
            deal = Deal.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            qs = store.customers.filter(total__gt=amount)
            if qs.exists():
                for i in qs:
                    i.rewards.add(deal)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})

#runs on end_date, if datetime == end_date, run task. to run right away set end_date to today,
#if start_date and end_date are equal, run tasks on that day and query that day only
#---
@shared_task
def special_day(content_uuid, store_uuid, release_date, type):
    if type == 'reward':
        try:
            reward = Reward.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            for i in store.customers:
                i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
    if type == 'deal':
        try:
            deal = Deal.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            for i in store.customers:
                i.rewards.add(deal)
        except (Deal.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})

@shared_task
def reward_after_purchase(content_uuid, store_uuid, item_uuid, start_date, end_date, type):
    if type == 'reward':
        try:
            reward = Reward.objects.get(uuid=reward_uuid)
            store = Store.objects.get(uuid=store_uuid)
            item = Item.objects.get(uuid=item_uuid)
            qs = store.customer.filter(tranactions__item__in=[item])
            if qs.exists():
                for i in qs:
                    i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
    elif type == 'deal':
        try:
            deal = Deal.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            item = Item.objects.get(uuid=item_uuid)
            qs = store.customer.filter(tranactions__item__in=[item])
            if qs.exists():
                for i in qs:
                    i.rewards.add(deal)
        except (Deal.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
#runs on end_date, if datetime == end_date, run task.
#if start_date and end_date are equal, run tasks on that day and query that day only

@shared_task
def spent_amount_within_time(content_uuid, store_uuid, amount, start_date, end_date, type):
    #activate application on end_date
    if type == 'reward':
        try:
            store = Store.objects.get(uuid=store_uuid)
            reward = Reward.objects.get(uuid=content_uuid)
            for i in store.customers:
                customer_amount = i.transaction.filter(date__range=[start_date, end_date]).aggregate(Sum('price'))
                if customer_amount >= amount:
                    i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})

    elif type == 'deal':
        try:
            store = Store.objects.get(uuid=store_uuid)
            deal = Deal.objects.get(uuid=content_uuid)
            for i in store.customers:
                customer_amount = i.transaction.filter(date__range=[start_date, end_date]).aggregate(Sum('price'))
                if customer_amount >= amount:
                    i.rewards.add(deal)
        except (Deal.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})
#APPLY AT THE MOMENT
@shared_task
def senior_customers(content_uuid, store_uuid, join_date, type):
    if type == 'reward':
        try:
            reward = Reward.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            qs = store.customers.filter(join_date__gt=join_date)
            if qs.exists():
                i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})

    elif type == 'deal':
        try:
            deal = Deal.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            qs = store.customers.filter(join_date__gt=join_date)
            if qs.exists():
                i.rewards.add(deal)
        except (Deal.DoesNotExist, Store.DoesNotExist):
            raise Response({'outcome': 'invalid query'})

@shared_task
def regular_reward(content_uuid, store_uuid, type):
    if type == 'reward':
        try:
            reward = Reward.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            for i in store.customers:
                i.rewards.add(reward)
            #    if i.settings.reward_notif == True:
                #    notify_celery_task(**kwargs)
        except (Reward.DoesNotExist, Store.DoesNotExist):
                raise Response({'outcome': 'invalid query'})

    elif type == 'deal':
        try:
            deal = Deal.objects.get(uuid=content_uuid)
            store = Store.objects.get(uuid=store_uuid)
            for i in store.customers:
                i.deals.add(deal)
            #    if i.settings.reward_notif == True:
                #    notify_celery_task(**kwargs)
        except (Deal.DoesNotExist, Store.DoesNotExist):
                raise Response({'outcome': 'invalid query'})

@shared_task
def in_favorites(content_uuid, store_uuid, item_uuid, type):
    if type == 'reward':
        try:
            item = Item.objects.get(uuid=item_uuid)
            store = Store.objects.get(uuid=customer_uuid)
            reward = Reward.objects.get(uuid=content_uuid)
            qs = store.customers.filter(favorites__item__in=item)#favorites.filter(item=item):
            if qs.exists():
                i.rewards.add(reward)
        except (Reward.DoesNotExist, Store.DoesNotExist):
                raise Response({'outcome': 'invalid query'})

    elif type == 'deal':
        try:
            item = Item.objects.get(uuid=item_uuid)
            store = Store.objects.get(uuid=customer_uuid)
            deal = Deal.objects.get(uuid=content_uuid)
            qs = store.customers.filter(favorites__item__in=item)#favorites.filter(item=item):
            if qs.exists():
                i.deals.add(deal)
        except (Deal.DoesNotExist, Store.DoesNotExist):
                raise Response({'outcome': 'invalid query'})

"""
HOW APPLICATION WORKS
THESE ARE ALL CELERY TASKS

BASED ON THE How_To_Apply, A CERTAIN FUCTION WILL CALLED WITH GIVEN ARGS. THEN THOSE FUNCTIONS WILL HANDLE
HOW TO APPLY AND WHEN TO APPLY REWARDS/DEALS

NOTIFICATIONS ARE CELERY TASK AND BASED ON THE CUSTOMER'S SETTINGS WILL BE CREATE A CELERY TASK.
WHICH IS CHECK WHEN APPLYING THE REWARD/DEAL
"""




















"""
FUTURE UPDATES


def random(reward_uuid, store_uuid):
    reward = reward.objects.get(uuid=reward_uuid)
    limit = reward.criteria.limit
    for i in store.customers(order_by=?)[300:800]:
        i.reward.add(reward)

def select_customers(reward_uuid, store_uuid, customers):
    pass
"""
