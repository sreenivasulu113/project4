from django.urls import path
from app2.views import *
app_name='san'
urlspatterns=[
    path('second/',second,name='second')
]