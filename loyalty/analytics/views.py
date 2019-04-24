from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from customer_user.models import Customer
from content.models import *
# Create your views here.
list all customers, by join date, age, gender, total money spent, points(ASC, DEC)
list customers that used certain rewards, by join date, age, gender, total money spent, points(ASC, DSC)

def ListByTraitsCustomers(request, params=[]):
    if request.user.store.exists():
        qs = request.user.customers.filter(join_date__gt=date)
        qs = request.user.customers.all().order_by('-birthdate')
        qs = request.user.customers.all().order_by('-total')
        qs = request.user.customers.all().order_by('-points')
        gender = request.GET.get('gender')
        if gender:
            qs = request.user.customers.filter(gender=gender)
            return render(request, 'html.html', {'qs':qs})

        return render(request, 'html.html', {'qs':qs})
        qs = model.objects.filter(l[0])
        l.pop()
        if len(l) > 1:
            for i in range(len(l)):
                qs = qs.filter(i)

def ListByTraitsCustomersUsingGender()

def ListByCustmersActivity(request, content_uuid):
    join_date = request.GET.get('join_date')
    age = request.GET.get('join_date')
    total = request.GET.get('total')
    points = request.GET.get('points')
    gender = request.GET.get('gender')
    order = request.GET.get('order')


    qs = request.user.customers.filter(used_reward__in=reward)
    if DSC == True:
        if join_date == True:
            qs.order_by('-join_date')
        elif age == True:
            qs.order_by('-age')
        elif total == True:
            qs.order_by('-total')
        elif points == True:
            qs.order_by('-points')
    else:
        if join_date == True:
            qs.order_by('join_date')
        elif age == True:
            qs.order_by('age')
        elif total == True:
            qs.order_by('total')
        elif points == True:
            qs.order_by('points')

    return render(request, 'html.html', {'qs':qs})
