from django.db import models
from store_user.models import Store
from customer_user.models import Customer


class StoreStripe(models.Model):
    store = OneToOneField(Store)
    card_id = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=255)

class CustomerStripe(models.Model):
    card_id = models.CharField(max_length=255)
    customer = ForeignKey(Customer, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.customer.CustomerStripe_set.count() > 5:
            return None
        else:
            return super(CustomerStripe, self).save(*args, **kwargs)

class Plan(models.Model):
    plan_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
