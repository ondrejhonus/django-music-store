from django.shortcuts import render
from .models import Instrument, InstrumentCategory, InstrumentType

def index(request):
    instruments = Instrument.objects.all().order_by('year').reverse()
    context = {
        'instruments': instruments,
        'categories': InstrumentCategory.objects.all(),
        }
    return render(request, 'index.html', context=context)

def instrument(request, category_slug):
    instruments = Instrument.objects.all()
    context = {
        'instruments': instruments.filter(type__category__slug=category_slug),
        'category': InstrumentCategory.objects.get(slug=category_slug),
        'types': InstrumentType.objects.filter(category__slug=category_slug),
        }
    return render(request, f'categories/all.html', context=context)

def instrument_type(request, category_slug, type_slug):
    if not InstrumentCategory.objects.filter(slug=category_slug).exists():
        return render(request, '404.html')
    if not InstrumentType.objects.filter(slug=type_slug, category__slug=category_slug).exists():
        return render(request, '404.html')
    instruments = Instrument.objects.filter(type__slug=type_slug, type__category__slug=category_slug)
    context = {
        'instruments': instruments,
        'type': InstrumentType.objects.get(slug=type_slug).name,
        'types': InstrumentType.objects.filter(category__slug=category_slug),
        'category': InstrumentCategory.objects.get(slug=category_slug).name,
        }
    return render(request, f'categories/type.html', context=context)

def instrument_detail(request, cat, slug):
    if not InstrumentType.objects.filter(category__slug=cat).exists():
        return render(request, '404.html')
    if not Instrument.objects.filter(type__category__slug=cat, slug=slug).exists():
        return render(request, '404.html')
    instrument = Instrument.objects.get(type__category__slug=cat, slug=slug)
    context = {
        'instrument': instrument,
        'category': InstrumentCategory.objects.get(slug=cat),
        'type': InstrumentType.objects.get(slug=instrument.type.slug),
        }
    return render(request, 'instruments/detail.html', context=context)

