# coding: utf-8

from django.contrib import admin
from django.urls import path, include
from member_info.views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]






