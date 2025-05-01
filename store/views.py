from django.shortcuts import render
from .models import Instrument, InstrumentCategory, InstrumentType

def index(request):
    instruments = Instrument.objects.all().order_by('year').reverse()
    context = {
        'instruments': instruments,
        }
    return render(request, 'index.html', context=context)

def instrument_detail(request, cat, slug):
    if not InstrumentType.objects.filter(category__slug=cat).exists():
        return render(request, '404.html')
    if not Instrument.objects.filter(type__category__slug=cat, slug=slug).exists():
        return render(request, '404.html')
    instrument = Instrument.objects.get(type__category__slug=cat, slug=slug)
    context = {
        'instrument': instrument,
        'category': InstrumentCategory.objects.get(slug=cat),
        }
    return render(request, 'instruments/detail.html', context=context)


##################################################
################### STRINGS ######################
##################################################

def strings(request):
    instruments = Instrument.objects.filter(type__category='1')
    context = {
        'instruments': instruments,
        }
    return render(request, 'categories/strings/all.html', context=context)

def string_type(request, type):
    if not InstrumentType.objects.filter(slug=type).exists():
        return render(request, '404.html')
    instruments = Instrument.objects.filter(type__slug=type)
    context = {
        'instruments': instruments,
        'type': InstrumentType.objects.get(slug=type).name,
        }
    return render(request, 'categories/strings/type.html', context=context)

###############################################
################# PERCUSSION ###################
###############################################

def percussion(request):
    instruments = Instrument.objects.filter(type__category='2')
    context = {
        'instruments': instruments
        }
    return render(request, 'categories/percussion/all.html', context=context)

def percussion_type(request, type):
    if not InstrumentType.objects.filter(slug=type).exists():
        return render(request, '404.html')
    instruments = Instrument.objects.filter(type__slug=type)
    context = {
        'instruments': instruments,
        'type': InstrumentType.objects.get(slug=type).name,
        }
    return render(request, 'categories/percussion/type.html', context=context)


################################################
################# KEYBOARDS ####################
################################################

def keyboards(request):
    instruments = Instrument.objects.filter(type__category='3')
    context = {
        'instruments': instruments,
        }
    return render(request, 'categories/keyboards/all.html', context=context)

def keyboard_type(request, type):
    if not InstrumentType.objects.filter(slug=type).exists():
        return render(request, '404.html')
    instruments = Instrument.objects.filter(type__slug=type)
    context = {
        'instruments': instruments,
        'type': InstrumentType.objects.get(slug=type).name,
        }
    return render(request, 'categories/keyboards/type.html', context=context)

###############################################
################# WIND #########################
###############################################

def wind(request):
    instruments = Instrument.objects.filter(type__category='4')
    context = {
        'instruments': instruments
        }
    return render(request, 'categories/wind/all.html', context=context)

def wind_type(request, type):
    if not InstrumentType.objects.filter(slug=type).exists():
        return render(request, '404.html')
    instruments = Instrument.objects.filter(type__slug=type)
    context = {
        'instruments': instruments,
        'type': InstrumentType.objects.get(slug=type).name,
        }
    return render(request, 'categories/wind/type.html', context=context)
