# Generated by Django 3.1.3 on 2020-11-08 03:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0012_delete_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='favorite_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
