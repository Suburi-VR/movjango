# Generated by Django 3.1.3 on 2020-11-27 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0035_merge_20201127_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='taggs',
        ),
    ]