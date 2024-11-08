from django.urls import path
from .views import ProjectListView, ProjectDetailView

urlpatterns = [
    path("project", ProjectListView.as_view(), name="project_list"),
    path("project/<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
]