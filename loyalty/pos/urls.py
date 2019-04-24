from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^all/$', views.getProducts, name='products'),
    url(r'^login/$', views.Login, name='login'),
]
