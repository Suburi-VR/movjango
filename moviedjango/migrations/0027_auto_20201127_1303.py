# Generated by Django 3.1.3 on 2020-11-27 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedjango', '0026_auto_20201127_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='tag1',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag10',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag2',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag3',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag4',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag5',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag6',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag7',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag8',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tag9',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
