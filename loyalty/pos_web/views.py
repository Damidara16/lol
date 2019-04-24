from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View
from .forms import *
#crud items, options, and categories

#ITEMS
def createItem(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, '', {'form':form})
    else:
        form = ItemCreationForm()
        return render(request, '', {'form':form})

def deleteItem(request, uuid):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            item.delete()
            return redirect(reverse())
        else:
            return render(request, '404.html')

def editItem(request, uuid):
    if request.method == 'PUT':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item, request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                return render(request, '', {'form':form})
        else:
            return render(request, '404.html')
    else:
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item)
            return render(request, '', {'form':form})
        else:
            return render(request, '404.html')

def detailItem(request, uuid):
    try:
        item = Item.objects.get(uuid=uuid)
    except Item.DoesNotExist:
        raise Http404("User does not exist")
    if item.store == request.user.store:
        try:
            analytics = ItemAnalytics.objects.get(item=item.uuid)
        except ItemAnalytics.DoesNotExist:
            raise Http404("Error retrieving item analytics")
        return render(request, '', {'item':item, 'analytics':analytics})
    else:
        return render(request, '404.html')

#categories
def createCategory(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, '', {'form':form})
    else:
        form = ItemCreationForm()
        return render(request, '', {'form':form})

def deleteCategory(request, uuid):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            item.delete()
            return redirect(reverse())
        else:
            return render(request, '404.html')

def editCategory(request, uuid):
    if request.method == 'PUT':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item, request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                return render(request, '', {'form':form})
        else:
            return render(request, '404.html')
    else:
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item)
            return render(request, '', {'form':form})
        else:
            return render(request, '404.html')

def detailCategory(request, uuid):
    try:
        item = Item.objects.get(uuid=uuid)
    except Item.DoesNotExist:
        raise Http404("User does not exist")
    if item.store == request.user.store:
        try:
            analytics = ItemAnalytics.objects.get(item=item.uuid)
        except ItemAnalytics.DoesNotExist:
            raise Http404("Error retrieving item analytics")
        return render(request, '', {'item':item, 'analytics':analytics})
    else:
        return render(request, '404.html')

#NOPTIONS
def createNOption(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, '', {'form':form})
    else:
        form = ItemCreationForm()
        return render(request, '', {'form':form})

def deleteNOption(request, uuid):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            item.delete()
            return redirect(reverse())
        else:
            return render(request, '404.html')

def editNOption(request, uuid):
    if request.method == 'PUT':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item, request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                return render(request, '', {'form':form})
        else:
            return render(request, '404.html')
    else:
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item)
            return render(request, '', {'form':form})
        else:
            return render(request, '404.html')

def detailNOption(request, uuid):
    try:
        item = Item.objects.get(uuid=uuid)
    except Item.DoesNotExist:
        raise Http404("User does not exist")
    if item.store == request.user.store:
        try:
            analytics = ItemAnalytics.objects.get(item=item.uuid)
        except ItemAnalytics.DoesNotExist:
            raise Http404("Error retrieving item analytics")
        return render(request, '', {'item':item, 'analytics':analytics})
    else:
        return render(request, '404.html')

#SOPTION
def createSOption(request):
    if request.method == 'POST':
        form = ItemCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, '', {'form':form})
    else:
        form = ItemCreationForm()
        return render(request, '', {'form':form})

def deleteSOption(request, uuid):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            item.delete()
            return redirect(reverse())
        else:
            return render(request, '404.html')

def editSOption(request, uuid):
    if request.method == 'PUT':
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item, request.POST, request.FILES)
            if form.is_valid():
                form.save()
            else:
                return render(request, '', {'form':form})
        else:
            return render(request, '404.html')
    else:
        try:
            item = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            raise Http404("User does not exist")
        if item.store == request.user.store:
            form = ItemCreationForm(instance=item)
            return render(request, '', {'form':form})
        else:
            return render(request, '404.html')

def detailSOption(request, uuid):
    try:
        item = Item.objects.get(uuid=uuid)
    except Item.DoesNotExist:
        raise Http404("User does not exist")
    if item.store == request.user.store:
        try:
            analytics = ItemAnalytics.objects.get(item=item.uuid)
        except ItemAnalytics.DoesNotExist:
            raise Http404("Error retrieving item analytics")
        return render(request, '', {'item':item, 'analytics':analytics})
    else:
        return render(request, '404.html')
