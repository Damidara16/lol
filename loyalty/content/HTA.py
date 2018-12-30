from django.db.models import Sum

#LONG RUNNING/AWAITED APPLICATION REWARDS
def special_day(release_date, reward_uuid, store_uuid):
    pass

def birthday(reward_uuid, store_uuid):
    pass

def total_spent_amount(reward_uuid, store_uuid, amount):
    pass

def new_user(store_uuid, customer_uuid, reward_uuid):
    store = Store.objects.get(uuid=store_uuid)
    reward = store.rewards.get(name=reward_name)
    customer = Customers.objects.get(uuid=customer_uuid)
    for i in store.reward_set.filter(criteria.How_To_Apply=new_user):
        kwargs['user'].rewards.add(i)

def reward_after_purchase(reward_uuid, store_uuid, item_uuid):
    pass

def spent_amount_within_time(reward_uuid, store_uuid, amount, start_date, end_date):
    #activate application on end_date
    store = Store.objects.get(uuid=store_uuid)
    reward = store.rewards.get(name=reward_name)
    for i in store.customers:
        customer_amount = i.transaction.filter(date__range=[start_date, end_date]).aggregate(Sum('price'))
        if customer_amount >= amount:
            i.rewards.add(reward)


#APPLY AT THE MOMENT
def senior_customers(reward_uuid, store_uuid, join_date):
    pass

def regular_reward(reward_uuid, store_uuid):
    reward = reward.objects.get(uuid=reward_uuid)
    for i in store.customers:
        i.reward.add(reward)
        if i.settings.reward_notif == True:
            notify_celery_task(**kwargs)

def in_favorites(item_uuid, store_uuid, reward_uuid):
    item = Item.objects.get(uuid=item_uuid)
    store = Store.objects.get(uuid=customer_uuid)
    reward = Reward.objects.get(uuid=reward_uuid)
    for i in store.customers.favorites.filter(item=item):
        customer.rewards.add(reward)

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
