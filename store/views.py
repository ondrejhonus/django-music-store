from django.shortcuts import render
from .models import Instrument

# Create your views here.

def index(request):
    instruments = Instrument.objects.all()
    context = {
        'instruments': instruments
        }
    return render(request, 'index.html', context=context)