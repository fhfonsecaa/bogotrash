# Generated by Django 2.0.9 on 2018-11-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bogotrash_app', '0004_auto_20181117_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queja',
            old_name='dirección',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='queja',
            old_name='geolocacion',
            new_name='geolocation',
        ),
    ]