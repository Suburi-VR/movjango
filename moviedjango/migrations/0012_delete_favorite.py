# Generated by Django 3.1.3 on 2020-11-06 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0011_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
