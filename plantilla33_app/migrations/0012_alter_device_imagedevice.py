# Generated by Django 3.2.10 on 2022-04-04 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla33_app', '0011_alter_device_imagedevice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='imageDevice',
            field=models.ImageField(upload_to='ImageDevices/'),
        ),
    ]
