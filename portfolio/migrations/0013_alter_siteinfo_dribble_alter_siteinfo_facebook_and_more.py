# Generated by Django 4.2 on 2023-06-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_mycv_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='dribble',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='facebook',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='pintarest',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='twitter',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='website_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]