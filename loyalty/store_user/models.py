from django.db import models
from django.contrib.auth.models import User
import random
import string
import uuid
from django.db.models.signals import post_save, pre_delete

def GenerateApiKey():
  l = []
  for u,_ in enumerate(range(10)):
    if u == 0 or u == 3 or u == 6 or u == 7 or u == 9:
      l.append(string.ascii_lowercase[random.randint(0, 25)])
    else:
      l.append(str(random.randint(1, 9)))

  return ''.join(l)

def gen2():
  l = ""
  for u,_ in enumerate(range(10)):
    if u == 0 or u == 3 or u == 6 or u == 7 or u == 9:
      l += string.ascii_lowercase[random.randint(0, 25)]
    else:
      l += str(random.randint(1, 9))

  return l
#no content conversion

#to improve lookup speed, try to sort the query

class Store(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Types = (('Sole','Sole'),('LLC','LLC'),('Corp','Corp'),)
    business_name = models.CharField(max_length=255)
    signup_ip_address = models.GenericIPAddressField()
    business_type = models.CharField(max_length=100, choices=Types)
    user = models.OneToOneField(User)
    api_key = models.CharField(max_length=10, default=GenerateApiKey(), editable=False, unique=True)
#user.store.customers.all()


class Address(models.Model):
    state = models.CharField(max_length=2)
    str1 = models.CharField(max_length=255)
    str2 = models.CharField(max_length=255)
    zipcode = models.PositiveIntegerField()
    store = models.OneToOneField(User)

#rm -f tmp.db db.sqlite3
#rm -r store_user/migrations


class Valid_Keys(models.Model):
    api_key = models.CharField(max_length=10, editable=False, unique=True)
    active = models.BooleanField(default=True)
    deactive = models.BooleanField(default=False)
    suspended = models.NullBooleanField(default=None)
    cancelled = models.NullBooleanField(default=None)

    def deactivate(self):
        self.active = False
        self.deactive = True
        self.save()
        return None

    def reactivate(self):
        self.active = True
        self.deactive = False
        self.save()
        return None

    def suspend(self):
        self.active = False
        self.deactive = False
        self.suspended = True
        self.save()
        return None

    def cancel(self):
        self.active = False
        self.deactive = False
        self.cancel = True
        self.save()
        return None

"""
    def save(self, *args, **kwargs):
        if self.active == True and self.deactive == True:
            if checkStoreStripe() == 'active':
                self.active = True
                self.deactive = False
                return super(Valid_Keys, self).save(*args, **kwargs)
            else:
                self.active = False
                self.deactive = True
                return super(Valid_Keys, self).save(*args, **kwargs)
        else:
            return super(Valid_Keys, self).save(*args, **kwargs)
"""









"""
SIGNALS SIGNALS SIGNALS
"""
def addApiKey(sender, **kwargs):
    if kwargs['created']:
        Valid_Keys.objects.create(api_key=kwargs['api_key'])
        #Valid_Keys.objects.create(api_key=kwargs['instance']['api_key'])

post_save.connect(addApiKey, sender=Store)

def deletedApiKey(sender, **kwargs):
    if kwargs['deleted']:
        ApiKey = Valid_Keys.objects.get(api_key=kwargs['api_key'])
        #Valid_Keys.objects.create(api_key=kwargs['instance']['api_key'])
        ApiKey.cancel()

pre_delete.connect(deletedApiKey, sender=Store)
