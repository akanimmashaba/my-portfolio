from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Project
# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'
    queryset = Project.objects.all()

def project_detail(request, slug):
    # Retrieve the project object or return a 404 error
    project = get_object_or_404(Project, slug=slug)

    # Pass the project object to the template
    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)