from django.db import models

# Create your models here.


from django.db import models
from ckeditor.fields import RichTextField

class PersonalInformation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    objective = RichTextField(blank=True, null=True)

class Education(models.Model):
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = RichTextField(blank=True, null=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])

class WorkExperience(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

class Course(models.Model):
    title = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    
class Certification(models.Model):
    title = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)

class Language(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.CharField(max_length=50, choices=[('Full professional proficiency', 'Full professional proficiency'), ('Native', 'Native'),('Elementry', 'Elementry'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = RichTextField(blank=True, null=True)

class SkillDetails(models.Model):
    title = models.CharField(max_length=100)
    
class ProfilePicture(models.Model):
    photo = models.ImageField(upload_to='photos/')
    
