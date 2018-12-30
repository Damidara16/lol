from django.shortcuts import render
from .models import Store

def CreateStore(request):
    if request.method == 'POST':
        form = StoreCreation(request.POST)
        if form.is_valid():
            form.save()
            return ...
        else:
            return ...

def viewProfile(request, name=None):
    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    if request.user.is_authenticated() == False:
        return render(request, "pages/1/privateprofile.html", {"user":user, 'unauthed':True})
    elif name == request.user.username:
        return render(request, "pages/1/ownerprofile.html", {"user":user})
    elif user.profile.private and user not in request.user.profile.following.all():
        return render(request, "pages/1/privateprofile.html", {"user":user})
    else:
        return render(request, "pages/1/viewprofile.html", {"user":user})

def updateProfile(request):
    if request.method  == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        form1 = UpdateUserForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and form1.is_valid():
            #profile = form.save(commit=False)
            #profile.first_name = form.cleaned_data['first_name']
            #profile.last_name = form.cleaned_data['last_name']
            #profile.email = form.cleaned_data['email']
            form.save()
            form1.save()
            return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))
        else:
            #messages.error(request, "Error")
            return render(request, 'pages/2/signup.html', {'form':form})

    else:
        form = EditProfileForm(instance=request.user)
        form1 = UpdateUserForm(instance=request.user.profile)
        return render(request, 'pages/5/editprofile.html', {'form':form, 'form1':form1})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            '''reg = form.save(commit=False)
            reg.email = form.cleaned_data['email']
            reg.username = form.cleaned_data['username']
            reg.first_name = form.cleaned_data['first_name']
            reg.last_name = form.cleaned_data['last_name']
            reg.password1 = form.cleaned_data['password1']
            reg.password2 = form.cleaned_data['password2']

            reg.save()'''
            return redirect(reverse('account:login'))

        else:
            #messages.error(request, "Error")
            return render(request, 'pages/2/signup.html', {'form':form})

    else:
        form = RegistrationForm()
        return render(request, 'pages/2/signup.html', {'form':form})

def deleteProfile(request):
    #add a re-enter passcode to delete account
    user = User.objects.get(uuid=request.user.uuid)
    user.delete()
    return redirect('/home')


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
            return ...
        else:
            return ...


def ListTransaction(request):
    pass

def CreateTransaction(request):
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

def TransactionDetails(request, uuid):
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
