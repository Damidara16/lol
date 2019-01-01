from django.db.models import Sum
from celery import Celery


#LONG RUNNING/AWAITED APPLICATION REWARDS
def special_day(release_date, reward_uuid, store_uuid):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    for i in store.customers:
        i.rewards.add(reward)

def birthday(reward_uuid, store_uuid):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    qs = store.customers.filter(birthday=datetime.now())
    #qs = store.customers.objects.filter()

def total_spent_amount(reward_uuid, store_uuid, amount):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    qs = store.customers.annotate(total=Sum('transactions__price'))
    for i in qs:
        if i.total > amount:
            i.rewards.add(reward)
    #IF USING TOTAL AMOUNT SPENT AFTER CERTAIN TIME

    for i in store.customers:
        total_amount = i.transactions.filter(date__gt=earilest_date_of_transaction).aggregate(Sum('price'))
        if total_amount > amount:
            i.rewards.add(reward)

#runs on end_date, if datetime == end_date, run task. to run right away set end_date to today,
#if start_date and end_date are equal, run tasks on that day and query that day only
def reward_after_purchase(reward_uuid, store_uuid, item_uuid, start_date, end_date=None):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    item = Item.objects.get(uuid=item_uuid)
    qs = store.customer.filter(tranactions__item__in=[item])
    for i in qs:
        i.rewards.add(reward)

#runs on end_date, if datetime == end_date, run task.
#if start_date and end_date are equal, run tasks on that day and query that day only
def spent_amount_within_time(reward_uuid, store_uuid, amount, start_date, end_date):
    #activate application on end_date
    store = Store.objects.get(uuid=store_uuid)
    reward = store.rewards.get(name=reward_name)
    for i in store.customers:
        customer_amount = i.transaction.filter(date__range=[start_date, end_date]).aggregate(Sum('price'))
        if customer_amount >= amount:
            i.rewards.add(reward)

#APPLY AT THE MOMENT
@task
def senior_customers(reward_uuid, store_uuid, join_date):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    for i in store.customers.filter(join_date__gt=join_date):
        i.rewards.add(reward)

@task
def regular_reward(reward_uuid, store_uuid):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    for i in store.customers:
        i.rewards.add(reward)
        if i.settings.reward_notif == True:
            notify_celery_task(**kwargs)

@task
def in_favorites(reward_uuid, store_uuid, item_uuid):
    item = Item.objects.get(uuid=item_uuid)
    store = Store.objects.get(uuid=customer_uuid)
    reward = Reward.objects.get(uuid=reward_uuid)
    for i in store.customers.filter(favorites__item__in=item):#favorites.filter(item=item):
        i.rewards.add(reward)


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
