from django.shortcuts import render

#list items and categories and transactions, sort by

#order by price, total sold, active_inventory, name,
#filter categories, noption, soption
#sort by combination -> by price, total sold, active_inventory for name, categories, noption, soption

def listItemAll(request):
    items = request.user.store.items
    return render(request, '', {'items':items})

def listItemBySort(request):
    query = Item.objects.all()
    type = request.GET.get('type')
    kwargs = {'{0}__{1}'.format('name', type): filterReq}
    if filterBy:
        query = query.filter(**kwargs)
    if orderBy and des:
        query = query.order_by('-' + orderBy)
    else:
        query = query.order_by(orderBy)
    return render(request, '', {'query':query})

def listCategory(request):
    cat = request.user.store.categories
    return render(request, '', {'cat':cat})

def listCategoryItems(request, name):
    cat = request.user.store.categories.get(name=name)
    items = cat.items.all()
    return render(request, '', {'items':item})
