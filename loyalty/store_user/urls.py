from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout
app_name = 'store_user'
urlpatterns = [
    url(r'^login/$', views.Login, name=''),
    url(r'^e/$', views.e, name='e'),
    url(r'^logout/$', logout, name=''),
    url(r'^profile/$', views.viewProfile, name=''),
    url(r'^update/$', views.updateProfile, name=''),
    url(r'^setup/$', views.createStore, name=''),
    url(r'^reg/$', views.registerUser, name=''),
    url(r'^delete/$', views.deleteProfile, name=''),
    url(r'^setup/$', views.customerDetails, name=''),
    url(r'^setup/$', views.deactivateCustomer, name=''),
    url(r'^setup/$', views.createTransaction, name=''),
    url(r'^setup/$', views.transactionDetails, name=''),
]
