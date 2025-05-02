from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, MaxLengthValidator, URLValidator

# Create your models here.

class InstrumentCategory(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="Enter the name of the instrument category (max 30 characters)",
        validators=[
            MinLengthValidator(2, "Category name must be at least 2 characters long."),
            MaxLengthValidator(30, "Category name cannot exceed 30 characters.")
        ],
    )
    description = models.TextField(
        help_text="Provide a description of the instrument category."
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Enter a unique slug for the category (max 50 characters)",
        validators=[
            MinLengthValidator(2, "Slug must be at least 2 characters long."),
            MaxLengthValidator(50, "Slug cannot exceed 50 characters.")
        ],
    )

    class Meta:
        verbose_name_plural = "Instrument Categories"

    def __str__(self):
        return self.name

class InstrumentType(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="Enter the type of instrument (max 30 characters)",
        validators=[
            MinLengthValidator(2, "Category name must be at least 2 characters long."),
            MaxLengthValidator(30, "Category name cannot exceed 30 characters.")
        ]
    )
    category = models.ForeignKey('InstrumentCategory', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(
        help_text="Provide a description of the instrument type."
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Enter a unique slug for the type (max 50 characters)",
        validators=[
            MinLengthValidator(2, "Slug must be at least 2 characters long."),
            MaxLengthValidator(50, "Slug cannot exceed 50 characters.")
        ],
    )

    def __str__(self):
        return self.name

class Instrument(models.Model):
    brand = models.CharField(
        max_length=30,
        help_text="Enter the brand name of the instrument (max 30 characters)",
        validators = [
            MinLengthValidator(2, "Brand name must be at least 2 characters long."),
            MaxLengthValidator(30, "Brand name cannot exceed 30 characters"),
        ],
    )
    model = models.CharField(
        max_length=100,
        help_text="Enter the model name of the instrument (max 100 characters)",
        validators=[
            MinLengthValidator(2, "Model name must be at least 2 characters long."),
            MaxLengthValidator(100, "Model name cannot exceed 100 characters")
        ],
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="Enter a unique slug for the instrument (max 100 characters)",
        validators=[
            MinLengthValidator(2, "Slug must be at least 2 characters long."),
            MaxLengthValidator(100, "Slug cannot exceed 100 characters.")
        ],
    )
    color = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Enter the color of the instrument (max 20 characters)",
        validators=[
            MinLengthValidator(2, "Color name must be at least 2 characters long."),
            MaxLengthValidator(20, "Color name cannot exceed 20 characters.")
        ]
    )
    description = models.TextField(
        help_text="Provide a detailed description of the instrument."
    )
    year = models.IntegerField(
        blank=True,
        null=True,
        help_text="Enter the year the instrument was manufactured.",
        validators=[
            MinValueValidator(1900, "Year must be 1900 or later."),
            MaxValueValidator(2100, "Year must be 2100 or earlier.")
        ]
    )
    type = models.ForeignKey(
        InstrumentType,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        help_text="Select one or more types for this instrument."
    )
    image = models.ImageField(
        upload_to='instruments/',
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