from django.shortcuts import render
from .models import Instrument

# Create your views here.

def index(request):
    instruments = Instrument.objects.all().order_by('year')
    context = {
        'instruments': instruments
        }
    return render(request, 'index.html', context=context)

def strings(request):
    instruments = Instrument.objects.filter(type__category='1')
    context = {
        'instruments': instruments
        }
    return render(request, 'categories/strings/all.html', context=context)

def percussion(request):
    instruments = Instrument.objects.filter(type__category='2')
    context = {
        'instruments': instruments
        }
    return render(request, 'categories/percussion/all.html', context=context)

def keyboards(request):
    instruments = Instrument.objects.filter(type__category='3')
    context = {
        'instruments': instruments
        }
    return render(request, 'categories/keyboards/all.html', context=context)

def wind(request):
    instruments = Instrument.objects.filter(type__category='4')
    context = {
        'instruments': instruments
        }
    return render(request, 'categories/wind/all.html', context=context)
