from django.db import models
from django.contrib.auth.models import User
import random
import string
import uuid
def GenerateApiKey():
  l = []
  for u,_ in enumerate(range(10)):
    if u == 0 or u == 3 or u == 6 or u == 7 or u == 9:
      l.append(string.ascii_lowercase[random.randint(0, 25)])
    else:
      l.append(str(random.randint(1, 9)))

  return ''.join(l)
#to improve lookup speed, try to sort the query

class Store(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Types = (('sole','sole'),('LLC','LLC'),('Corp','Corp'))
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
