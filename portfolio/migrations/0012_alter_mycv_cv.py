# Generated by Django 4.2 on 2023-06-04 18:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_mycv_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycv',
            name='cv',
            field=models.FileField(upload_to='cv/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
    ]
