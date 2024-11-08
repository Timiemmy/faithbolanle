from django.db import models


class Project(models.Model):
    project_title = models.CharField(max_length=200, blank=True, null=True)
    project_description = models.TextField(blank=True, null=True)
    project_image = models.ImageField(upload_to='project_images', blank=True, null=True)
    project_link = models.URLField(max_length=200, blank=True, null=True)
    project_github_link = models.URLField(max_length=200, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)