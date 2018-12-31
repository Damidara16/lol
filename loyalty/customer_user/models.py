from django.db import models
from django.contrib.auth.models import User
import uuid
from store_user.models import Store
from content.models import Reward, Deal, Tranaction, Item

class Customer(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    store = models.ForeignKey(Store, related_name='customers', on_delete=models.CASCADE)
    birthdate = models.DateTimeField()
    phone_number =  models.CharField(max_length=10, validators=['validation_phone_number'])
    Gender = (('male','male'), ('female','female'), ('other','other'))
    gender = models.CharField(max_length=10, choices=Gender)
    active = models.BooleanField(default=True)
    signup_ip_address = models.GenericIPAddressField()
    total_spent = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    rewards = models.ManyToManyField(Reward)
    deals = models.ManyToManyField(Deal)
    used_rewards = models.ManyToManyField(Reward)
    used_deals = models.ManyToManyField(Deal)
    visits = models.PositiveIntegerField(default=0)
    transactions = models.ForeignKey(Tranaction, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Item)
    #visits = num of transaction
    #store must be requested ip addresses via email request

    def validation_phone_number(self):
        if self.phone_number.isdecimal():
            return ValidationError('only numbers, no (), - , or extensions')


#user.customer.store
#when adding store in shell must save the customer object not the user,
#ex. good: user.customer.save(), bad: user.save()
