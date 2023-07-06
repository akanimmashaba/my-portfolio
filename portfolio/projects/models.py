from django.db import models
from resume.models import Resume

# Create your models here.
# Projects
class Project(models.Model):
    """
    # projects
    
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='protjects')
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    contribution = models.TextField()
    github = models.URLField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/images', blank=True, null=True)

    def __str__(self):
        return str(self.title)