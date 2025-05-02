from django.shortcuts import redirect, render
from .models import Instrument, InstrumentCategory, InstrumentType
from .forms import UserRegistrationForm, InstrumentForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    instruments = Instrument.objects.all().order_by('year').reverse()
    context = {
        'instruments': instruments,
        'categories': InstrumentCategory.objects.all(),
        }
    return render(request, 'index.html', context=context)

def search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        instruments = Instrument.objects.filter(
            brand__icontains=search_query
        ).union(
            Instrument.objects.filter(model__icontains=search_query)
        ).order_by('year').reverse()
        context = {
            'instruments': instruments,
            'categories': InstrumentCategory.objects.all(),
            }
        return render(request, 'index.html', context=context)
    else:
        return redirect('index')

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
        'can_edit': request.user.is_staff or request.user.groups.filter(name='editor').exists(),
        }
    return render(request, 'instruments/detail.html', context=context)

def instrument_create(request):
    if request.method == 'POST':
        form = InstrumentForm(request.POST, request.FILES)
        if form.is_valid():
            instrument = form.save()
            instrument.user = request.user
            instrument.save()
            return redirect('index')
    else:
        form = InstrumentForm()
    context = {
        'form': form,
        }
    return render(request, 'actions/create.html', context=context)


def instrument_delete(request, cat, slug):
    if not InstrumentType.objects.filter(category__slug=cat).exists():
        return render(request, '404.html')
    if not Instrument.objects.filter(type__category__slug=cat, slug=slug).exists():
        return render(request, '404.html')
    instrument = Instrument.objects.get(type__category__slug=cat, slug=slug)
    if request.method == 'POST':
        instrument.delete()
        return redirect('index')
    context = {
        'instrument': instrument,
        }
    return render(request, 'actions/confirm-delete.html', context=context)

def instrument_update(request, cat, slug):
    if not InstrumentType.objects.filter(category__slug=cat).exists():
        return render(request, '404.html')
    if not Instrument.objects.filter(type__category__slug=cat, slug=slug).exists():
        return render(request, '404.html')
    instrument = Instrument.objects.get(type__category__slug=cat, slug=slug)
    if request.method == 'POST':
        form = InstrumentForm(request.POST, request.FILES, instance=instrument)
        if form.is_valid():
            form.save()
            return redirect('instrument_detail', cat=cat, slug=slug)
    else:
        form = InstrumentForm(instance=instrument)
    context = {
        'form': form,
        'instrument': instrument,
        }
    return render(request, 'actions/update.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        }
    return render(request, 'users/register.html', context=context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
            
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('login')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html')
    else:
        return redirect('login')
