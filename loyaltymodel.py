



#a.customer.rewards.add(reward)












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
