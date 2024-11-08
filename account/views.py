from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Information, Education, Experience, About, Social_links, Tool
from project.models import Project

class Home(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['information'] = Information.objects.all()
        context['experience'] = Experience.objects.all().order_by('-end_date')
        context['education'] = Education.objects.all()
        context['projects'] = Project.objects.all().order_by('-created_date')
        context['skills'] = Tool.objects.all()
        context['about'] = About.objects.all()
        context['socials'] = Social_links.objects.all()
        return context