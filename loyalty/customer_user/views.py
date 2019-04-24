from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer
from rest_framework.authtoken.views import ObtainAuthToken
from store_user.models import Store
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.generics import RetrieveAPIView, ListAPIView
from content.models import Reward, Deal
#THIS VIEW HANDLES ALL API REQUEST VERIFICATIONS BECUASE A USER NEEDS A API KEY TO LOGIN AND GET THEIR TOKEN
#SO IF THEY WERE ABLE TO GET THEN TOKEN THEN ALL OTHER REQUEST USE BE AUTHED.
@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        valid_keys = Valid_Keys.objects.fitler(active=True).values_list('api_key', flat=True).order_by('api_key')
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            if request.data['api_key'] in valid_keys:
                user = authenticate(**serializer.validated_data)
                if user is not None:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token':token.key, 'outcome':'success'})
                else:
                    return Response({'outcome':'failure to authorize'})
            else:
                return Response({'outcome':'error 8320, please contact us for more help'})



@api_view(['POST'])
def CreateCustomer(request, api_key):
    if request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            store = Store.objects.get(api_key=request.POST['api_key'])
            serializer.save(store=store)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'PUT'])
def EditCustomer(request):
    if request.method == 'POST':
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def DeleteCustomer(request):
    pass

@api_view(['GET'])
def RewardDealFeed(request):
    if request.method == 'GET':
        rewards = request.user.rewards.all()
        serializer = RewardSerializer(rewards, many=True)
        deals = request.user.deals.all()
        serializer1 = DealSerializer(deals, many=True)
        result = {**serializer.data, **serializer1.data}
        return Response(result)

@api_view(['GET'])
def UsedRewardDealFeed(request):
    if request.method == 'GET':
        used_rewards = request.user.used_rewards.all()
        serializer = RewardSerializer(used_rewards, many=True)
        used_deals = request.user.used_deals.all()
        serializer1 = DealSerializer(used_deals, many=True)
        result = {**serializer.data, **serializer1.data}
        return Response(result)

@api_view(['GET'])
def TransactionFeed(request):
    if request.method == 'GET':
        transaction = request.user.transactions_set.all()
        serializer = TransactionSerializers(transaction, many=True)
        return Response(serializer.data)


def TransactionValidator(method_of_payment, date, store, items=[]):
    #check if the transaction already belongs to another user
    if Transaction.customer.exists() and not request.user:
        pass

def AddTransactionToCustomer(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            result = TransactionValidator(**serializer.data)
            if result[0] == 'valid':
                t = Transaction.objects.get(uuid=result[1])
                request.user.transactions.add(t)


class TransactionDetail(RetrieveAPIView):
    serializer_class = TransactionSerializer
    #permission_classes = (IsUser,)
    lookup_field = 'uuid'
    queryset = Transaction.objects.all()

class RewardDetail(RetrieveAPIView):
    serializer_class = RewardSerializer
    #permission_classes = (IsUser,)
    lookup_field = 'uuid'
    queryset = Deal.objects.all()

class DealDetail(RetrieveAPIView):
    serializer_class = DealSerializer
    #permission_classes = (IsUser,)
    lookup_field = 'uuid'
    queryset = Deal.objects.all()


def index(request):
    customer = Customer.objects.all()
    store = Store.objects.get(business_name='bakery')
    rewards = store.reward_set.filter(criteria__applications='new user')
    print(rewards)
    #deals = store.deal_set.filter(criteria__applications='new user')
    if rewards.exists():
        for i in rewards:
            for x in store.customers.all():
                print(x)
                x.rewards.add(i)
    return JsonResponse({'eje':'ho'}, safe=False)
