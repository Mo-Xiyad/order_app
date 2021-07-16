# Generated by Django 3.2.4 on 2021-07-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower', '0008_alter_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flower',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='start_datetime',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='time',
        ),
        migrations.RemoveField(
            model_name='flower',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='flower',
            name='ordered_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
