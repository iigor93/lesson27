# Generated by Django 4.0.4 on 2022-05-14 15:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.CharField(default=0, max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=False,
        ),
    ]
