from .models import Resume

def active_resume(request):
    resume = Resume.objects.filter(is_active=True).first()
    return {'active_resume': resume}