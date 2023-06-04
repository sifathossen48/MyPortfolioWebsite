from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class SiteInfo(models.Model):
    logo = models.ImageField(upload_to='site_picture/')
    favicon = models.ImageField(upload_to='site_picture/')
    profile = models.ImageField(upload_to='site_picture/')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    work_place = models.CharField(max_length=60)
    about_description = models.TextField()
    about_description2 = models.TextField()
    costomers_no =models.CharField(max_length=20)
    costomers_desc = models.TextField()
    projects_completed = models.CharField(max_length=20)
    projects_desc = models.TextField()
    lines_of_code = models.CharField(max_length=20)
    lines_of_code_desc = models.TextField()
    feedback_no = models.CharField(max_length=20)
    feedback_desc = models.TextField()
    facebook = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    dribble = models.CharField(max_length=100, blank=True)
    pintarest = models.CharField(max_length=100, blank=True)
    more_website_name = models.CharField(max_length=50)
    website_link = models.CharField (max_length=100, blank=True)
    phone_no = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    contact_desc = models.TextField(max_length=300)
    copyright_site_name = models.CharField(max_length=40)
    designer_name = models.CharField(max_length=50)
    designer_profile_link = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Experience(models.Model):
    tool = models.CharField(max_length=50)
    work_title = models.CharField(max_length=50)
    def __str__(self):
        return self.tool

class Skill (models.Model):
    skill_name = models.CharField(max_length=50)
    def __str__(self):
        return self.skill_name

class Awards (models.Model):
    name = models.CharField(max_length=30)
    awards_link = models.CharField(max_length=100)
    category_and_time = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Work (models.Model):
    image = models.ImageField(upload_to='work/')
    title = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    description = models.TextField(max_length=250)
    project_link = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    image = models.ImageField(upload_to='clients/')
    client_name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.client_name

class MyCV(models.Model):
    name =models.CharField(max_length=50)
    cv = models.FileField(upload_to='cv/', validators=[FileExtensionValidator(['pdf'])])
    def __str__(self):
        return self.name