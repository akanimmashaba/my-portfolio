
from django.urls import path
from . import views 
urlpatterns = [
    path('', views.ProjectListView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', views.project_detail, name='project-detail'),
]
