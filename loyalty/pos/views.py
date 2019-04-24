from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from store_user.models import Store
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from .serializers import *
from store_user.serializers import *
from rest_framework.generics import RetrieveAPIView, ListAPIView
from content.models import *
from rest_framework.permissions import IsAuthenticated



@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        serializer = LoginPosSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'outcome':'success', 'token':token.key})
            else:
                return Response({'outcome':'failure to authorize'})

@api_view(['POST'])
def getProducts(request):
    if request.method == 'POST':
        if request.user.is_authenicated():
            categories = request.user.categories
            results = ProductSerializers(data=categories, many=True)
            return Response(results)
        else:
            return Response({'outcome':'failure to authorize'})

@api_view(['GET'])
#react does the checking, it calls the url and gets json reponse and checks if its the same, if not make next request
def getUpdate(request):
    if request.method == 'GET':
        if request.user.is_authenicated():
            lastest_code = request.user.UpdateKey.lastest()
            return JsonResponse({'updated':True, 'code':'lastest_code'})
        else:
            return Response({'outcome':'failure to authorize'})



def sendAnalytics(request):
    pass

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
#figure out how to make it only one call to the db instead of two
def checkInv(request):
    if request.method == 'POST':
        serializer = InvItemSerializer(data=request.data)
        if serializer.is_valid():
            a = []
            for i in serializer.data['items']:
                b = request.user.store.item_set.get(abbr=i.abbr)
                if i.amount > b.active_inventory
                    a.append({i.name:b.active_inventory})
            if a != []:
                return Response({'excedded':True, 'excedded_items':a})
            else:
                for x in serializer.data['items']:
                    b = request.user.store.item_set.get(abbr=x.abbr)
                    b.active_inventory -= x.amount
                    b.save()
                return Response({'outcome':'clear'})

@api_view(['POST'])
def UpdateInv(request):
    if request.method == 'POST':
        serializer = InvItemCancelSerializer(data=request.data)
        if serializer.is_valid():
            for i in serializer.data['items']:
                b = request.user.store.item_set.get(abbr=i.abbr)
                b.active_inventory += i.amount
                b.save()
                return Response({'outcome':'success'})

#costly request
@api_view(['POST'])
def sendCart(request):
    if request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            transaction = Transaction(store=request.user.store, price=serializer.data['metadata']['price'],
            transaction_id=serializer.data['metadata']['transaction_id'],
            orderNum=serializer.data['metadata']['orderNum'],
            method_of_payment=serializer.data['metadata']['mop'])
            for i in serializer.data['items']:
                try:
                    a = Item.objects.get(name=i.name)
                    d = cartItem.objects.create(item=a)
                    for ii in i.option.noptions:
                        try:
                            b = ItemNumOption.objects.get(name=ii.name)
                            r = CartItemNumOption.object.create(applied=ii.applied, store=b.store,
                            name=b.name, applications_amount=ii.amount)
                            d.noption.add(r)
                        except ItemNumOption.DoesNotExist:
                            continue
                    for x in i.option.soptions:
                        try:
                            c = ItemSelectOption.objects.get(name=x.name)
                            w = CartItemNumOption.object.create(applied=x.applied, store=c.store,
                            name=c.name, selected=x.selected)
                            d.soption.add(w)
                        except ItemSelectOption.DoesNotExist:
                            continue
                transaction.cartItem.add(d)
            transaction.save()
