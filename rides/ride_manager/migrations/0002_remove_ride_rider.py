# Generated by Django 5.0.1 on 2024-01-13 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ride_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='rider',
        ),
    ]
