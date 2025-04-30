from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

# Create your models here.

class InstrumentCategory(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.name

class InstrumentType(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="Enter the type of instrument (max 30 characters)",
        )
    description = models.TextField()

    def __str__(self):
        return self.name


class Instruments(models.Model):
    brand = models.CharField(
        max_length=30,
        help_text="Enter the brand name of the instrument (max 30 characters)",
        validators = [
            MinLengthValidator(2, "Brand name must be at least 2 characters long.")
        ]
    )
    model = models.CharField(
        max_length=20,
        help_text="Enter the model name of the instrument (max 20 characters)",
        validators=[
            MinLengthValidator(2, "Model name must be at least 2 characters long.")
        ]
    )
    description = models.TextField(
        help_text="Provide a detailed description of the instrument."
    )
    year = models.IntegerField(
        help_text="Enter the year the instrument was manufactured.",
        validators=[
            MinValueValidator(1900, "Year must be 1900 or later."),
            MaxValueValidator(2100, "Year must be 2100 or earlier.")
        ]
    )
    category = models.ManyToManyField(
        InstrumentCategory,
        help_text="Select one or more categories for this instrument."
    )
    type = models.ManyToManyField(
        InstrumentType,
        help_text="Select one or more types for this instrument."
    )
    image = models.ImageField(
        upload_to='images/',
        help_text="Upload an image of the instrument."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Enter the price of the instrument (max 10 digits, 2 decimal places).",
        validators=[
            MinValueValidator(0.01, "Price must be greater than zero.")
        ]
    )
    stock = models.IntegerField(
        help_text="Enter the number of items in stock.",
        validators=[
            MinValueValidator(0, "Stock cannot be negative.")
        ]
    )

    def __str__(self):
        return self.brand + ' ' + self.model
    

    class Manufacturer(models.Model):
        name = models.CharField(max_length=50, unique=True)
        country = models.CharField(max_length=50, blank=True, null=True)
        description = models.TextField()
        website = models.URLField(max_length=200, blank=True, null=True)

        def __str__(self):
            return self.name
        
