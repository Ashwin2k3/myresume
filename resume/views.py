from django.shortcuts import render

# Create your views here.


from .models import PersonalInformation, Education, Skill, WorkExperience, Project, Certification, Language, Achievement,Course

def resume(request):
    personal_info = PersonalInformation.objects.first()
    education = Education.objects.all()
    skills = Skill.objects.all()
    work_experience = WorkExperience.objects.all()
    projects = Project.objects.all()  # Add projects data
    certifications = Certification.objects.all()  # Add certifications data
    languages = Language.objects.all()  # Add languages data
    achievements = Achievement.objects.all()  # Add achievements data
    courses = Course.objects.all() # Add courses data

    context = {
        'personal_info': personal_info,
        'education': education,
        'skills': skills,
        'work_experience': work_experience,
        'projects': projects,
        'certifications': certifications,
        'languages': languages,
        'achievements': achievements,
        'courses' : courses,
        
    }

    return render(request, 'resume.html', context)




