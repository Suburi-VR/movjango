# Generated by Django 3.1.2 on 2020-10-30 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0008_auto_20201030_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movies',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
