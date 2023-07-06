from django.contrib import admin
from .models import Resume, WorkExperience, Education, Skill, Hobbies,Contacts


class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 1


class EducationInline(admin.StackedInline):
    model = Education
    extra = 1


class SkillInline(admin.StackedInline):
    model = Skill
    extra = 1


class HobbiesInline(admin.StackedInline):
    model = Hobbies
    extra = 1


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInline, EducationInline, SkillInline, HobbiesInline]
    list_display = ('full_name', 'email', 'phone_number')
    search_fields = ('full_name', 'email', 'phone_number')
    list_filter = ('full_name', 'email')


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'job_title', 'start_date', 'end_date')
    search_fields = ('company', 'job_title')
    list_filter = ('company', 'start_date', 'end_date')


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'graduation_year')
    search_fields = ('institution', 'degree', 'graduation_year')
    list_filter = ('institution', 'degree', 'graduation_year')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


@admin.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
     
    list_display = ('name',)
    search_fields = ('email',)
    list_filter = ('massage',)
