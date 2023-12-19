# Generated by Django 5.0 on 2023-12-19 05:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('shop_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('shop_name', models.CharField(max_length=100)),
                ('shop_address', models.CharField(max_length=100)),
                ('shop_type', models.CharField(max_length=100)),
                ('shop_number', models.CharField(max_length=13)),
            ],
        ),
    ]