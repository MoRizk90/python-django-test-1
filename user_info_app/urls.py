from django.urls import path, re_path, include
from django.urls import re_path
from user_info_app import views

print('hh')

urlpatterns = [

    re_path(r'^$',views.user,name = 'user'),
 



]
