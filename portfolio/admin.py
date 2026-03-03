from django.contrib import admin
from .models import Project, SkillCategory, Skill, ProjectImage, ProjectDocument, ProjectArchitecture, Resume, ArchitectureSection, ArchitecturePrinciple, ArchitectureLayer, AboutPage, AboutHighlight, ContactPage, ContactMessage
# Register your models here.

#1=============================================================
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

class ProjectDocumentInline(admin.TabularInline):
    model = ProjectDocument
    extra = 1

class ProjectArchitectureInline(admin.StackedInline):
    model = ProjectArchitecture
    extra = 0

class ArchitectureLayerInline(admin.TabularInline):
    model = ArchitectureLayer
    extra = 1

class AboutHighlightInline(admin.TabularInline):
    model = AboutHighlight
    extra = 1
#1=============================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('category', 'is_featured')
    search_fields = ('title',)
    inlines = [ProjectImageInline,
               ProjectDocumentInline,
               ]


#===========================================
# SKILLS SECTION

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'order')
    list_filter = ('category',)

#==================================================

#==================================================
# Create Resume Model
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at', 'is_active')

#=======================================================
# Architecture Principles (Structured)
class ArchitecturePrincipleInline(admin.TabularInline):
    model = ArchitecturePrinciple
    extra = 1


@admin.register(ArchitectureSection)
class ArchitectureSectionAdmin(admin.ModelAdmin):
    inlines = [ArchitecturePrincipleInline]

@admin.register(ProjectArchitecture)
class ProjectArchitectureAdmin(admin.ModelAdmin):
    inlines = [ArchitectureLayerInline]

@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    inlines = [AboutHighlightInline]

#==============================================================
@admin.register(ContactPage)
class ContactPageAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject")