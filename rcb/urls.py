from django.urls import path
from rcb.views import *
app_name='any'

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]