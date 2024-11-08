from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project



class ProjectListView(ListView):
    template_name = "project.html"
    queryset = Project.objects.all()

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
