from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Resume, WorkExperience, Education, Skill, Hobbies, Reference


def index(request):
    # Get any necessary data from models or other sources
    data = {
    }
    
    # Render the index.html template with the data
    return render(request, 'index.html', context=data)



def resume_detail(request):
    # Retrieve the resume object or return a 404 error
    resume = get_object_or_404(Resume.objects.all().order_by('id')[:1])

    # Get related objects using the reverse relationships defined in the models
    work_experiences = resume.experience.all()
    educations = resume.education.all()
    skills = resume.skills.all()
    hobbies = resume.hobbies.all()
    references = resume.references.all()

    # Pass the resume object to the template
    context = {
        'resume': resume
    }
    return render(request, 'resume_detail.html', context)
