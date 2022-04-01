# Generated by Django 3.2.10 on 2022-04-01 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantilla33_app', '0006_auto_20220401_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='placed',
            field=models.CharField(choices=[('COL', 'COLOMBIA'), ('ARG', 'ARGENTINA'), ('BRA', 'BRASIL'), ('CHI', 'CHILE')], max_length=3),
        ),
    ]