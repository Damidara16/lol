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
