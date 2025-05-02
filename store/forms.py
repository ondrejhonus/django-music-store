from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Instrument, InstrumentType, InstrumentCategory

from django import forms
from .models import Instrument


class InstrumentForm(forms.ModelForm):
    class Meta:
        model = Instrument
        fields = [
            'brand',
            'model',
            'slug',
            'color',
            'description',
            'year',
            'type',
            'price',
            'stock',
            'image',
        ]
        widgets = {
            'description': forms.Textarea(),
        }
        error_messages = {
            'brand': {
                'required': 'Brand is required.',
                'max_length': 'Brand name cannot exceed 30 characters.',
            },
            'model': {
                'required': 'Model is required.',
                'max_length': 'Model name cannot exceed 100 characters.',
            },
            'slug': {
                'required': 'Slug is required.',
                'max_length': 'Slug cannot exceed 100 characters.',
            },
            'color': {
                'max_length': 'Color name cannot exceed 20 characters.',
            },
            'description': {
                'required': 'Description is required.',
            },
            'year': {
                'invalid': 'Enter a valid year.',
            },
            'price': {
                'required': 'Price is required.',
                'invalid': 'Enter a valid price.',
            },
            'stock': {
                'invalid': 'Enter a valid stock quantity.',
            },
            'type': {
                'required': 'Type is required.',
            },
            'image': {
                'required': 'Upload an image of the instrument.',
                'invalid': 'Upload a valid image file.',
            }
        }

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year and (year < 1900 or year > 2100):
            raise forms.ValidationError('Year must be between 1900 and 2100.')
        return year

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        return stock if stock is not None else 0


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user