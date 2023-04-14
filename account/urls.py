from django.contrib import admin
from django.urls import path,include
from account.views import signup,login,logout

urlpatterns = [
    path('register',signup,name='signup'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),

]