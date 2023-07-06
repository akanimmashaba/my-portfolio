from django.db import models


class Resume(models.Model):
    # Personal Information
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=11,blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to='blog/images', blank=True, null=True)
    personal_statement = models.TextField()
    cv = models.FileField("cv", upload_to="resume", max_length=100)

class WorkExperience(models.Model):
    """
    Work Experience
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    achievements = models.TextField(blank=True)

class Education(models.Model):
    """
    # Education
    
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    graduation_year = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return str(self.institution)
        
# Skills
class Skill(models.Model):
    """
    skills
    
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Hobbies(models.Model):
    """
    Hobbies
    
    """
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='hobbies')

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

# References (not included in the model, but can be stored in a separate model if needed)
class Reference(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='references')
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return str(self.title)

class Contacts(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    massage = models.TextField()

    def __str__(self):
        return self.name
    
    