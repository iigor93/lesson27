# Generated by Django 4.0.4 on 2022-05-14 17:03

import authentication.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_address',
            field=models.EmailField(default=0, max_length=254, unique=True, validators=[authentication.models.no_rambler]),
            preserve_default=False,
        ),
    ]
