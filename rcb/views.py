from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(request):
    return HttpResponse('<h1>when rcb wins the cup</h1>')
