# Generated by Django 3.2.4 on 2021-07-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0013_alter_order_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_no',
            field=models.IntegerField(default='', help_text='Contact phone number'),
        ),
    ]
