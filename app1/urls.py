from django.urls import path
from app1.views import *
app_name='archi'
urlspatterns=[
    path('first/',first,name='first')
]