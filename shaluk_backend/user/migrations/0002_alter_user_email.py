# Generated by Django 5.0 on 2023-12-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This value must be unique.'}, max_length=255, unique=True, verbose_name='Email'),
        ),
    ]
