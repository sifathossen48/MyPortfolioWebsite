# Generated by Django 4.2 on 2023-05-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='site_picture/')),
                ('favicon', models.ImageField(upload_to='site_picture/')),
                ('profile', models.ImageField(upload_to='site_picture/')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('work_place', models.CharField(max_length=60)),
                ('about_description', models.TextField()),
                ('about_description2', models.TextField()),
                ('costomers_no', models.CharField(max_length=20)),
                ('costomers_desc', models.TextField(max_length=100)),
                ('projects_completed', models.CharField(max_length=20)),
                ('projects_desc', models.TextField(max_length=100)),
                ('lines_of_code', models.CharField(max_length=20)),
                ('lines_of_code_desc', models.TextField(max_length=100)),
                ('feedback_no', models.CharField(max_length=20)),
                ('feedback_desc', models.TextField(max_length=100)),
                ('facebook', models.CharField(max_length=100)),
                ('instagram', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('dribble', models.CharField(max_length=100)),
                ('pintarest', models.CharField(max_length=100)),
                ('more_website_name', models.CharField(max_length=50)),
                ('website_link', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=50)),
                ('contact_desc', models.TextField()),
                ('copyright_site_name', models.CharField(max_length=40)),
                ('designer_name', models.CharField(max_length=50)),
                ('designer_profile_link', models.CharField(max_length=100)),
            ],
        ),
    ]
