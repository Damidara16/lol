from django.db.models import Sum

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
    """
    for i in store.customers:
        total_amount = i.transactions.filter(date__gt=earilest_date_of_transaction).aggregate(Sum('price'))
        if total_amount > amount:
            i.rewards.add(reward)
    """


def new_user(store_uuid, customer_uuid, reward_uuid):
    store = Store.objects.get(uuid=store_uuid)
    reward = store.rewards.get(name=reward_name)
    customer = Customers.objects.get(uuid=customer_uuid)
    for i in store.reward_set.filter(criteria__How_To_Apply=new_user):
        kwargs['user'].rewards.add(i)

def reward_after_purchase(reward_uuid, store_uuid, item_uuid, earilest_date_of_purchase):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    item = Item.objects.get(uuid=item_uuid)
    qs = store.customer.filter(tranactions__item__in=[item])
    for i in qs:
        i.rewards.add(reward)


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
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
    for i in store.customers.filter(join_date>join_date):
        i.rewards.add(reward)


def regular_reward(reward_uuid, store_uuid):
    reward = Reward.objects.get(uuid=reward_uuid)
    store = Store.objects.get(uuid=store_uuid)
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
