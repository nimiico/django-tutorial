# Generated by Django 4.2.5 on 2023-09-06 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(max_length=360, null=True),
        ),
    ]