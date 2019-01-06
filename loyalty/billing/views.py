from django.shortcuts import render
from django.conf import settings
# Create your views here.
def CancelPlan(request):
    code = request.user.StoreStripe.subscription_id
    sub = stripe.Subscription.retrieve(code)
    sub.at_period_end = true
    return render(request)

def AddPlan(request):
    try:
        request.user.store
        if request.user.StoreStripe.customer_id:
            request.user.StoreStripe.subscription_id = ...

    except:
        return Response('Action Not Allowed')
