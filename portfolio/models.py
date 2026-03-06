from django.db import models
import cloudinary.models

# Create your models here.

class Project(models.Model):

    CATEGORY_CHOICES = (
        ('ecommerce', 'E-Commerce'),
        ('ai_agent', 'AI Agent'),
        ('rag', 'RAG System'),
        ('ml', 'Machine Learning'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    full_description = models.TextField()

    tech_stack = models.TextField(help_text="Comma separated technologies")

    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    thumbnail = cloudinary.models.CloudinaryField('image')

    created_at = models.DateTimeField(auto_now_add=True)

    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    @property
    def tech_stack_list(self):
        if self.tech_stack:
            return [line.strip() for line in self.tech_stack.split('\n') if line.strip()]
        return []

#======================================================
# For SKILLS  Selection

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(
        SkillCategory,
        related_name='skills',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name 
    
#==========================================================

#==========================================================
# Additional Project Assets

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.project.title} - Image"


class ProjectDocument(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='documents',
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='projects/documents/')

    def __str__(self):
        return f"{self.project.title} - {self.title}"


class ProjectArchitecture(models.Model):
    project = models.OneToOneField(
        Project,
        related_name='architecture',
        on_delete=models.CASCADE
    )

    headline = models.CharField(max_length=200)
    subtitle = models.TextField()

    overview_title = models.CharField(
        max_length=200,
        default="Architecture Overview"
    )

    def __str__(self):
        return f"{self.project.title} - Architecture"
    
#==========================================================

#==========================================================
# Create Resume Model
class Resume(models.Model):
    title = models.CharField(max_length=200, default="My Resume")
    file = models.FileField(upload_to='resume/')
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
#===========================================================
# Architecture Principles (Structured)

class ArchitectureSection(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()

    def __str__(self):
        return self.title


class ArchitecturePrinciple(models.Model):
    section = models.ForeignKey(
        ArchitectureSection,
        related_name="principles",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    why_it_matters = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
    
#=============================================================================
# ArchitectureLayer Model
class ArchitectureLayer(models.Model):
    architecture = models.ForeignKey(
        ProjectArchitecture,
        related_name='layers',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.architecture.project.title} - {self.title}"
    
#=========================================================================

# ==========================================
# ABOUT PAGE
# ==========================================

class AboutPage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    intro_paragraph = models.TextField()

    profile_image = models.ImageField(upload_to="about/", blank=True, null=True)

    def __str__(self):
        return "About Page"


class AboutHighlight(models.Model):
    about = models.ForeignKey(
        AboutPage,
        related_name="highlights",
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


# ==========================================
# CONTACT PAGE CONTENT
# ==========================================

class ContactPage(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    intro_text = models.TextField()

    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return "Contact Page"


# ==========================================
# CONTACT MESSAGE STORAGE
# ==========================================

class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
#===============================================================
