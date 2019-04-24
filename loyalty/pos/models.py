from django.db import models
from content.models import *




"""
    for i in item['options']:
        if type == 'numOption' and applied == True:
            a = self.item.option.get(name=i.name)
            a.uuid = None
            a.item=self.item
            a.applied=True
            a.applications_amount = i.num
            a.save()
"""

"""
1. copy item option
2. add option to cart item
3. update option inventory

then do a matching query for lookup

so if new transaction has been made, a push to all device to update inventory for the items and options

pos updates
inventory

pos design updated on new carts or manually reset




HAVE A CHECK IF IN STOCK VIEW FOR ITEM AND OPTION COUNT
"""
