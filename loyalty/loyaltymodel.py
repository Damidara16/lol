from django.models impor models




#a.customer.rewards.add(reward)


class MetaInfo(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    user = models.ForeignKey(Cusotmer)

class Favorites(models.Model):
    items = models.ManyToMany(Item)
    user = models.ForeignKey(User)


class Store_Plan(models.Model):
    Plans = (('1', '1'),('2','2'), ('3','3'))
    plan = models.CharField(max_length=2, choices=Plans)
    store = models.ForeignKey(Store)
    active = models.BooleanField(default=True)


class Item(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntergerField(default=0)
    store = models.ForeignKey(Store)
    item_serial_id = models.CharField(max_length=255)


class Redeemed(models.Model):
    times_used = models.PositiveIntergerField(default=0)
    customer = models.OneToOne(User)
    firsted_redeemed = models.DateTimeField()
    reward = models.ManyToMany


class Parent_Rewards_Deals(models.Model):
    Discount_Type = (('free','free'), ('percent_discount','percent_discount'), ('amount_discount','amount_discount'))

    type = models.CharField(max_length=255 choices=Discount_Type)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_add_now=True)
    store = models.ForeignKey('Store', on_delete=Models.CASCADE)
    description = models.CharField(max_length=255)
    notification_slogan = models.CharField(max_length=255)
    criteria = models.ForeignKey('Criteria', on_delete=Models.CASCADE)
    expired = models.BooleanField(default=False)
    times_used = models.PositiveIntergerField(default=0)


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

    class Meta:
        abstrast = True

class reward(Parent_Rewards_Deals):
    pass

class deal(Parent_Rewards_Deals):
    pass



class transaction(models.Model):
    store = models.ForeignKey(Store)
    customer = models.ForeignKey(User)
    transaction_id = models.CharField(max_length=255)
    price = models.PositiveIntergerField(default=0)
    reward_used = models.BooleanField(null=True)



class Criteria(models.Model):
    How_To_Apply = (('total spent amount','total spent amount'), ('spent amount within time', 'spent amount within time'), ('new user','new user'),
    ('reward after purchase','reward after purchase'), ('birthday','birthday'), ('random','random'), ('special days','special days'),
    ('senior customers','senior customers'), ('regular reward','regular reward'), ('in favorites','in favorites'), ('select customers', 'select customers'))
    percent = models.PositiveIntergerField(null=True)
    amount = models.PositiveIntergerField(null=True)
    terms_rules = models.CharField(max_length=500)
    limited_uses = models.PositiveIntergerField(null=True)
    expires = models.DateTimeField(null=True)
    applications = models.CharField(max_length=50, choices=How_To_Apply)

    #BASED ON THE How_To_Apply A SIGNAL WILL SEND THE NEWLY CREATED 'REWARD' TO VIEW WHICH WILL CREATE THE PROPER PROCESSES


"""
NOTIFY CUSTOMER WHEN NEW REWARD HAS BEEN ADDED TO THEIR REWARD LIST, USING THE NOTIFICATION SLOGAN TO TELL THEM WHAT IT ITS. SO USING A SIGNAL TO PUSH A TASK TO CELERY TO NOTFIY THEM
SO FIGURE OUT HOW TO KNOW WHEN NEW REWARD HAS BEEN ADDED AND HOW TO ADD REWARD ON MASS SCALE TO ALL USERS

USING A FOR LOOP,
EX
FOR I IN USERS.OBJECTS.FILTER(STORE=...).FILTER(JOINED=...)
    I.REWARDS.ADD(REWARD)
OR
FOR I IN USERS.OBJECTS.FILTER(STORE=...)
    IF ITEM IN I.TRANSCATION.FILTER(FROM DATE TILL NOW):
        I.REWARDS.ADD(REWARD)

THIS IS MAYBE CPU INTENSIVE IF STORES HAVE 1000+ CUSTOMERS, THERE MAY BE A MORE EFFIECENT WAY BUT FOR NOW THIS IS HOW IT WORKS

HAVE CELERY CHECK IF THE REWARD IS STILL CREATED IN CASE THE STORE DELETES THE REWARD SHORTLY AFTER MAKING IT.
"""


"""
CONCERNS

HOW TO HANDLE ALWAYS ON POINTS?
HOW TO HANDLE ON EVENT REWARDS?
"""

"""
class points(models.Model):
    amount
    store
    user
class Point_Criteria(models.Model):
    How_To_Apply = (('total spent amount','total spent amount'), ('spent amount within time', 'spent amount within time'), ('new user','new user'),
    ('points after purchase','points after purchase'), ('birthday','birthday'), ('certain items bought',' certain items bought'))
    amount = models.PositiveIntergerField(null=True)
    applications = models.CharField(max_length=50, choices=How_To_Apply)
"""
