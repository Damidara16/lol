from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    Types = (('sole','sp'),('LLC','LLC'),('Corp','Corp'))
    business_name = models.CharField(max_length=255)
    signup_ip_address = models.GenericIPAddressField()
    business_type = models.CharField(max_length=100, choices=Types)
    user = models.OneToOneField(User)
#user.store.customers.all()

class Customer(models.Model):
    name = models.CharField(max_length=255)
    signup_ip_address = models.GenericIPAddressField()
    user = models.OneToOneField(User)
    store = models.ForeignKey(Store, related_name='customers', on_delete=models.CASCADE, null=True)
#user.customer.store
#when adding store in shell must save the customer object not the user,
#ex. good: user.customer.save(), bad: user.save()
class Address(models.Model):
    state = models.CharField(max_length=2)
    str1 = models.CharField(max_length=255)
    str2 = models.CharField(max_length=255)
    zipcode = models.PositiveIntegerField()
    store = models.OneToOneField(User)

#rm -f tmp.db db.sqlite3
#rm -r store_user/migrations
