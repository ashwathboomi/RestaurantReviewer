# Generated by Django 4.2 on 2023-08-10 19:50

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='popular_review',
            new_name='review',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='star_rating',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='name_of_restaurant',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.FloatField(default=50, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='time',
            field=models.DateField(default=datetime.date(2023, 8, 10)),
        ),
    ]
