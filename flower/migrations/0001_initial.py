# Generated by Django 3.2.4 on 2021-07-09 13:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BouquetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bouquet_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large')], max_length=10)),
                ('amount', models.IntegerField()),
                ('start_datetime', models.DateTimeField(blank=True, default=datetime.datetime.today, null=True)),
                ('return_date', models.TimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(null=True)),
                ('bouquet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.bouquettype')),
            ],
        ),
        migrations.CreateModel(
            name='DateWithTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('planed_date', models.DateField(default=datetime.date.today)),
                ('start_datetime', models.DateTimeField(blank=True, default=datetime.datetime.today, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime.today)),
                ('bouquet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.bouquettype')),
            ],
        ),
    ]
