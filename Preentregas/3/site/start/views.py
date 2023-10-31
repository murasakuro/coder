from django.shortcuts import render
from start.models import Product

def welcome(request):
    return render(request, 'start.html', {})

def 