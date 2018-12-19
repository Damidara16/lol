from django.shortcuts import render
from .models import Customer
from store_user.models import Store
# Create your views here.

def CreateCustomer(request, api_key):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                store = Store.objects.get(api_key=request.POST['api_key'])
                serializer.save(store=store)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def Login(request):
    #get user info then validate the api_key and then check if user is in store customers
    pass
@api_view(['GET'])
def RewardFeed(request):
    if request.method == 'GET':
        rewards = request.user.rewards.all()
        serializer = RewardFeed(rewards, many=True)
        deals = request.user.deals.all()
        serializer1 = RewardFeed(deals, many=True)
        return Response(serializer.data + serializer1.data,)

@api_view(['GET'])
def UsedRewardFeed(request):
    if request.method == 'GET':
        used_rewards = request.user.used_rewards.all()
        serializer = RewardFeed(used_rewards, many=True)
        used_deals = request.user.used_deals.all()
        serializer1 = RewardFeed(used_deals, many=True)
        return Response(serializer.data + serializer1.data,)

@api_view(['GET'])
def TransactionFeed(request):
    if request.method == 'GET':
        transaction = request.user.transactions_set.all()
        serializer = TransactionSerialers(transaction, many=True)
        return Response(serializer.data + serializer1.data,)
