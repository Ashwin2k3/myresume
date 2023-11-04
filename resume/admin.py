from django.contrib import admin
from django.contrib import admin
from .models import PersonalInformation, Education, Skill,SkillDetails, Course, WorkExperience, Project, Certification, Language, Achievement
from django import forms

# Register your models here.

@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    pass  # This will use the default form for PersonalInformation

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass  # This will use the default form for Education

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass  # This will use the default form for Skill

@admin.register(SkillDetails)
class SkillDetailsAdmin(admin.ModelAdmin):
    pass

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    pass  # This will use the default form for WorkExperience

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass  # This will use the default form for Project

# @admin.register(Course)
# class Course(admin.ModelAdmin):
#     pass

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass  # This will use the default form for Certification

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass  # This will use the default form for Language

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    pass  # This will use the default form for Achievement

