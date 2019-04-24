from django.contrib import admin

from .models import Reward, Deal, Transaction, Item, MetaInfo, Criteria, Category

admin.site.register(Reward)
admin.site.register(Deal)
admin.site.register(Transaction)
admin.site.register(Item)
admin.site.register(MetaInfo)
admin.site.register(Criteria)
admin.site.register(Category)
