from django.urls import path
from csk.views import *
app_name='any'

urlpatterns=[
    path('msdhoni/',msdhoni,name='msdhoni'),
]