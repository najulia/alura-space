# Generated by Django 4.1.5 on 2023-02-01 00:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_publicacao',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
