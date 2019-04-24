from django.db import models
from content.models import *

class ItemAnalytics(models.Model):
    clicks = models.ForeignKey()
    cancelled = models.ForeignKey()
    avg_order_bundle_num = models.PostiveInteger()
    item = models.OneToOneField()

class Clicks(models.Model):
    date = models.PostiveInteger()

class Cancelled(models.Model):
    date = models.PostiveInteger()


"""
create a singal for each item

item clicks !
options selection - query matching
items sold - item field query
checkout times - transactions field query
number of cancelled items !
transactions method - transactions field query
"""
