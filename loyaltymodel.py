



#a.customer.rewards.add(reward)





class Store_Plan(models.Model):
    Plans = (('1', '1'),('2','2'), ('3','3'))
    plan = models.CharField(max_length=2, choices=Plans)
    store = models.ForeignKey(Store)
    active = models.BooleanField(default=True)








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
