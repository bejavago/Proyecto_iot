# Generated by Django 4.0.3 on 2022-04-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='nombre',
            field=models.CharField(default=None, max_length=45, unique=True, verbose_name='Nombre'),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=45, unique=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(default=None, max_length=200, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=None, max_length=72),
        ),
    ]
