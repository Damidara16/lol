from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^api-token-auth/', views.Login.as_view(), name='login')
    url(r'^login/$', views.Login, name='login')

]
