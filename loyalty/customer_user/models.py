from django.db import models
from django.contrib.auth.models import User
import uuid
from store_user.models import Store
from content.models import Reward, Deal, Transaction, Item
from django.db.models.signals import post_save

class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    store = models.ForeignKey(Store, related_name='customers', on_delete=models.CASCADE)
    rewards = models.ManyToManyField(Reward, blank=True)
    deals = models.ManyToManyField(Deal, blank=True)
    used_rewards = models.ManyToManyField(Reward, related_name='used_rewards', blank=True)
    used_deals = models.ManyToManyField(Deal, related_name='used_deals',blank=True)
    visits = models.PositiveIntegerField(default=0)
    #transactions = models.ForeignKey(Transaction, on_delete=models.CASCADE, blank=True)
    favorites = models.ManyToManyField(Item, blank=True)
    birthdate = models.DateTimeField()
    phone_number =  models.CharField(max_length=10)
    Gender = (('male','male'), ('female','female'), ('other','other'))
    gender = models.CharField(max_length=10, choices=Gender)
    active = models.BooleanField(default=True)
    signup_ip_address = models.GenericIPAddressField()
    join_date = models.DateTimeField(auto_now_add=True)
    total_spent = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    #visits = num of transaction
    #store must be requested ip addresses via email request

    def validation_phone_number(self):
        if self.phone_number.isdecimal():
            return ValidationError('only numbers, no (), - , or extensions')


#user.customer.store
#when adding store in shell must save the customer object not the user,
#ex. good: user.customer.save(), bad: user.save()

def New_User_Reward(sender, instance, created, **kwargs):
    if created:
        store = kwargs['instance'].store
        rewards = store.reward_set.filter(criteria__applications='new user')
        #deals = store.deal_set.filter(criteria__applications='new user')
        if rewards.exists():
            for i in rewards:
                instance.rewards.add(i)
        #if deals.exists():
        #    for x in deals:
        #        kwargs['instance'].deals.add(x)


post_save.connect(New_User_Reward, sender=Customer)
