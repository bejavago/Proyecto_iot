# Generated by Django 4.0.3 on 2022-04-06 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla33_app', '0015_alter_device_imagedevice'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_id',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.CharField(choices=[('Arduino UNO', 'Arduino UNO'), ('Raspberry', 'Raspberry'), ('ESP8266', 'ESP8266'), ('ESP32', 'ESP32')], max_length=20),
        ),
    ]
