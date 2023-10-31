from django.shortcuts import render
from start.models import Die, DiceBag

def welcome(request):
    return render(request, 'start.html', {})

def dice(request):
    die=Die(style='Mica Swirl Violeta y Negro', faces=20, numbering='Blanco')
    die.save()
    return render(request, 'die.html', {'die':die})