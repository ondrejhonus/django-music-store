# Generated by Django 5.2 on 2025-05-02 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_instrument_type_instrument_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manufacturer',
        ),
    ]
