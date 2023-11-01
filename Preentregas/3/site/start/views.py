from django.shortcuts import render
from start.models import Die, DiceBag, Tray

def welcome(request):
    return render(request, 'start/start.html', {})

def dice(request):
    die=Die(style='Mica Swirl Violeta y Negro', faces=20, numbering='Blanco')
    die.save()
    return render(request, 'start/die.html', {'die':die})

def dice_bag(request):
    dice_bag=DiceBag(material='Cuero Vacuno', color='Violeta', capacity='100')
    dice_bag.save()
    return render(request, 'start/dice_bag.html', {'dice_bag':dice_bag})

def tray(request):
    tray=Tray(material='Pino forrado en fieltro', color='Natural', size='1')
    tray.save()
    return render(request, 'start/tray.html', {'tray':tray})