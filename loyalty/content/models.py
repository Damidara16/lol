from django.db import models
from store_user.models import Store
from django.contrib.auth.models import User
import uuid
from .HTA import regular_reward, in_favorites, senior_customers
"""
class Redeemed(models.Model):
    times_used = models.PositiveIntegerField(default=0)
    customer = models.OneToOneField(User)
    firsted_redeemed = models.DateTimeField()
    reward = models.ForeignKey('Reward')
"""

class Criteria(models.Model):
    #BASED ON THE HTA A CERTAIN FORM WILL APPEAR
    How_To_Apply = (('lifetime total spent amount','lifetime total spent amount'), ('spent amount within time', 'spent amount within time'), ('new user','new user'),
    ('reward after purchase','reward after purchase'), ('birthday','birthday'), ('special day','special day'),
    ('senior customers','senior customers'), ('regular reward','regular reward'), ('in favorites','in favorites'),)
    terms_rules = models.CharField(max_length=500)
    single_use = models.BooleanField(default=True)
    expires = models.DateTimeField(null=True)#if null == forever
    applications = models.CharField(max_length=50, choices=How_To_Apply)
    join_date = models.DateTimeField(null=True)
    item_uuid = models.CharField(max_length=50, null=True)
    amount = models.PositiveIntegerField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    release_date = models.DateTimeField(null=True)

class Parent_Rewards_Deals(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    criteria = models.OneToOneField(Criteria, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Discount_Type = (('free','free'), ('percent_discount','percent_discount'), ('amount_discount','amount_discount'),)
    type = models.CharField(max_length=255, choices=Discount_Type)
    percent = models.PositiveIntegerField(null=True)
    amount = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    notification_slogan = models.CharField(max_length=255)
    times_used = models.PositiveIntegerField(default=0)
    deactive_application = models.BooleanField(default=False)

    class Meta:
        abstract = True
"""
#THIS CALLS THE CELERY TASK
    def save(self, *args, **kwargs):
        if self.criteria.applications == 'regular reward':
            regular_reward.delay(self.uuid, self.store.uuid)

        elif self.criteria.applications == 'senior customers':
            senior_customers.delay(self.uuid, self.store.uuid)

        elif self.criteria.applications == 'in favorites':
            in_favorites.delay(self.uuid, self.store.uuid)

        elif self.criteria.applications == 'lifetime_total_spent_amount':
            lifetime_total_spent_amount.delay(self.uuid, self.store.uuid, self.criteria.amount)
"""

"""
AFTER A REWARD IS USED IT WILL BE REMOVED FROM A CUSTOMERS REWARDS TO USED, STORES CAN SEE WHO USED THEIR REWARD THEY DO,
A = STORE.REWARDS_SET.ALL()[0]
FOR I IN STORE.CUSTOMERS:
    IF A IN I.USED_REWARDS:
    LIST.APPEND(I)
    RETURN LIST
THIS A EXSPENSIVE TASK, OPTIMIZATION IS NEEDED

IF THE REWARD HAS UNLIMITED, IT WILL CHECK MODEL BEFORE REMOVING
"""


class Reward(Parent_Rewards_Deals):
    Reward = (('reward', 'reward'),)
    reward_tag = models.CharField(max_length=20, choices=Reward, default='reward', editable=False)

#    def save(self, *args, **kwargs):
#        celeryTask(self.uuid)


class Deal(Parent_Rewards_Deals):
    Deal = (('deal', 'deal'),)
    deal_tag = models.CharField(max_length=20, choices=Deal, default='deal', editable=False)

#    def save(self, *args, **kwargs):
#        celeryTask(self.uuid)


class MetaInfo(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    item_key = models.CharField(max_length=50)
    item_value = models.CharField(max_length=50)


class Item(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    item_serial_id = models.CharField(max_length=255, null=True)


class Transaction(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=0)
    reward_used = models.NullBooleanField(default=None)

"""
    def save(self, *args, **kwargs):
        if self.customer:
            customer = Customer.objects.get(uuid=uuid)
            customer.transactions.add(self)
            customer.total_spent += self.price
            customer.save()
        return super(Transaction, self).save(*args, **kwargs)
"""


        #user m2m signal to update customer total
"""
NOTIFY CUSTOMER WHEN NEW REWARD HAS BEEN ADDED TO THEIR REWARD LIST, USING THE NOTIFICATION SLOGAN TO TELL THEM WHAT IT ITS.
SO USING A SIGNAL TO PUSH A TASK TO CELERY TO NOTFIY THEM SO FIGURE OUT HOW TO KNOW WHEN NEW REWARD
HAS BEEN ADDED AND HOW TO ADD REWARD ON MASS SCALE TO ALL USERS

USING A FOR LOOP,
EX
FOR I IN USERS.OBJECTS.FILTER(STORE=...).FILTER(JOINED=...)
    I.REWARDS.ADD(REWARD)
    URL = I.NOTIFICATION.URL
    NOTIFY(URL)#THIS MIGHT HAUL UP CELERY, SENDING THE NOTFIY TASK TO CELERY MAY GIVE IT ROOM TO OTHER TASKS

    OR

    URL = I.NOTIFICATION.URL
    CELERY_NOTIFY(URL)#PUSHES A NEW TASK TO CELERY

OR
FOR I IN USERS.OBJECTS.FILTER(STORE=...)
    IF ITEM IN I.TRANSCATION.FILTER(FROM DATE TILL NOW):
        I.REWARDS.ADD(REWARD)

THIS IS MAYBE CPU INTENSIVE IF STORES HAVE 1000+ CUSTOMERS, THERE MAY BE A MORE EFFIECENT WAY BUT FOR NOW THIS IS HOW IT WORKS

HAVE CELERY CHECK IF THE REWARD IS STILL CREATED IN CASE THE STORE DELETES THE REWARD SHORTLY AFTER MAKING IT.
"""
