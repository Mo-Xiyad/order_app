# Generated by Django 3.2.4 on 2021-07-09 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0004_alter_flower_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flower',
            old_name='return_date',
            new_name='time',
        ),
    ]