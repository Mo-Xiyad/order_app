# Generated by Django 3.2.4 on 2021-07-09 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='flower',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]