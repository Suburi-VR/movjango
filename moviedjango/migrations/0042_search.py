# Generated by Django 3.1.3 on 2020-12-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0041_remove_movie_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.TextField(max_length=200)),
            ],
        ),
    ]