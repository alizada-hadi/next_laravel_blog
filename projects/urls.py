from django.urls import path
from . import views


urlpatterns = [
    path("projects/", views.get_project_list, name="project_list"),
    path("project/new/", views.create_project_view, name="create_project"),
]
