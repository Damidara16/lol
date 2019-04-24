from django.shortcuts import render, redirect
from .models import Store
from django.contrib.auth import authenticate
from .forms import *
from django.urls import reverse


def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            if Store.objects.filter(user__username=form.cleaned_data['username']).exists():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    return redirect(reverse('store_user:e'))
            else:
                return redirect(reverse('store_user:e'))
                    #return render(request, 'store_user/create.html', {'form':form})
    else:
        form = LoginForm()
        return render(request, 'store_user/create.html', {'form':form})

def e(request):
    return render(request, 'store_user/j.html')

def createStore(request):
    if request.method == 'POST':
        form = StoreCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('store_user:profile'))
        else:
            return render(request, 'store_user/create.html', {'form':form})


def viewProfile(request, name=None):
    if request.user.store.exists():
        return render(request, "store_user/profile.html", {"user":request.user})
    else:
        return redirect(reverse('home:home'))

def updateProfile(request):
    if request.method  == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        form1 = UpdateUserForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and form1.is_valid():
            form.save()
            form1.save()
            return redirect(reverse('store_user:profile'))
        else:
            return render(request, 'pages/2/signup.html', {'form':form})
    else:
        form = EditProfileForm(instance=request.user)
        form1 = UpdateUserForm(instance=request.user.profile)
        return render(request, 'pages/5/editprofile.html', {'form':form, 'form1':form1})

def registerUser(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:login'))

        else:
            return render(request, 'pages/2/signup.html', {'form':form})
    else:
        form = RegistrationForm()
        return render(request, 'pages/2/signup.html', {'form':form})

def deleteProfile(request):
    #add a re-enter passcode to delete account
    if request.method == 'POST':
        form = DeleteProfile(request.POST)
        if request.user.check_password(form.cleaned_data['password']):
            user = User.objects.get(uuid=request.user.uuid)
            user.delete()
            return redirect(reverse('home:home'))
    else:
        return redirect(reverse('home:home'))

def customerDetails(request, uuid):
    try:
        customer = request.user.customers.get(uuid=uuid)
    except Customer.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, 'store_user/customerDetails.html', {'customer',customer})

def deactivateCustomer(request, uuid):
    if request.method == 'POST':
        form = UpdateCustomer(request.POST, instance=Customer)
        if form.is_valid():
            form.save(commit=False)
            model.activate = form.cleaned_data['activate']
            model.save()
            return redirect(reverse())
        else:
            return render(request, 'store_user/')


def createTransaction(request):
    if request.method == 'POST':
        form = RewardCreationForm(request.POST)
        form = CriteriaCreationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            reward = form.save(commit=False)
            form1.save()
            reward.criteria = form1
            reward.save()
            return redirect(reverse())
        else:
            return render()

def transactionDetails(request, uuid):
    if request.method == 'POST':
        form = RewardCreationForm(request.POST)
        form = CriteriaCreationForm(request.POST)
        if form.is_valid() and form1.is_valid():
            reward = form.save(commit=False)
            form1.save()
            reward.criteria = form1
            reward.save()
            return ...
        else:
            return ...
