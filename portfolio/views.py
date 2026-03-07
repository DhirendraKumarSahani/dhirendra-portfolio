from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, SkillCategory, ArchitectureSection, AboutPage, ContactPage, ContactMessage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    featured_projects = Project.objects.filter(is_featured=True)
    skill_categories = SkillCategory.objects.prefetch_related('skills')
    architecture_section = ArchitectureSection.objects.prefetch_related('principles').first()

    context = {
        'featured_projects': featured_projects,
        'skill_categories': skill_categories,
        'architecture_section': architecture_section,
    }

    return render(request, 'portfolio/home.html', context)


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/project_list.html', {
        'projects': projects
    })


def project_detail(request, slug):
    project = get_object_or_404(Project.objects.select_related('architecture'), slug=slug)

    tech_list = []
    if project.tech_stack:
        tech_list = [tech.strip() for tech in project.tech_stack.split(',')]

    return render(request, 'portfolio/project_detail.html', {
        'project': project,
        'tech_list': tech_list 
    })

#============================================================================
# AboutPage

def about(request):
    about_page = AboutPage.objects.prefetch_related("highlights").first()

    return render(request, "portfolio/about.html", {
        "about": about_page
    })
#============================================================================

#============================================================================
def contact(request):
    contact_page = ContactPage.objects.first()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save in database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("contact")

    return render(request, "portfolio/contact.html", {
        "contact_page": contact_page
    })
#=================================================================================
