# Generated by Django 3.2.9 on 2021-11-30 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='name',
            field=models.CharField(default='', max_length=25),
        ),
    ]
