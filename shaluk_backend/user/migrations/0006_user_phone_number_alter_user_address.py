# Generated by Django 5.0 on 2023-12-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='01944700614', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='CUET', max_length=255),
        ),
    ]
