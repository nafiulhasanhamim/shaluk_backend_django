# Generated by Django 5.0 on 2023-12-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='01944700614', max_length=15),
        ),
    ]
