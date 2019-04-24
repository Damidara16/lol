from django.shortcuts import render
from django.conf import settings
# Create your views here.
def viewPlan(request):
    pass

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

@api_view(['POST'])
def addValidateCardCustomer(request):
    if request.method == 'POST':
        serializer = CardSerializer(request.data)
        if serializer.is_valid():
            a = stripe.Card.create(serializer.data['four'], serializer.data['exp'], serializer.data['sec'])
            if a.status == 'valid':
                CustomerStripe.objects.create(card_id=a.id, customer=serializer.data['customer'])
            else:
                return Response({'outcome':'card could not be verified'})

@api_view(['POST'])
def replaceBillingInfo(request):
    current_card = customer.CustomerStripe
    if a.status== 'valid':
        current_card.delete()
        CustomerStripe.objects.create()
