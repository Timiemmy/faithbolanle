from django.db import models
from django.contrib.auth.models import User


class Information(User):
    description = models.TextField(null=True, blank=True)
    resume = models.FileField(upload_to='resume', null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic', null=True, blank=True)

    class Meta:
        verbose_name = "User Information"

    def __str__(self):
        return str(self.first_name)

class About(models.Model):
    image = models.ImageField(upload_to='about_pic', blank=True, null=True)
    about = models.TextField(blank=True, null=True)



class Social_links(models.Model):
    linkedin = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    twitter = models.CharField(max_length=200, blank=True, null=True)


class Education(models.Model):
    institution = models.CharField(max_length=200, blank=True, null=True)
    degree = models.CharField(max_length=100, blank=True, null=True)
    field_of_study = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.institution} - {self.degree}"


class Experience(models.Model):
    company = models.CharField(max_length=200, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    current = models.BooleanField(default=False)
    description = models.TextField( blank=True, null=True)

    def __str__(self):
        return f"{self.company} - {self.position}"

class Tool(models.Model):
    tool_name = models.CharField(max_length=100, blank=True, null=True)
    

    def __str__(self):
        return self.tool_name