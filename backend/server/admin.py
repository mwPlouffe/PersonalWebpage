from django.contrib import admin
from .models import *



class AdminSkill(admin.ModelAdmin):
    list_display = ('type', 'name')


class AdminInterest(admin.ModelAdmin):
    list_display = ('type', 'name')


class AdminAssociation(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'city', 'start', 'end')


class AdminEducation(admin.ModelAdmin):
    list_display = ('name', 'university', 'city', 'start', 'end')


class AdminEducationNote(admin.ModelAdmin):
    list_display = ('education', 'item')


class AdminProject(admin.ModelAdmin):
    list_display = ('name', 'place', 'city', 'start', 'end', 'personal')


class AdminProjectNote(admin.ModelAdmin):
    list_display = ('project', 'item')


class AdminWork(admin.ModelAdmin):
    list_display = ('name', 'company', 'city', 'start', 'end', 'volunteer')


class AdminWorkNote(admin.ModelAdmin):
    list_display = ('work', 'item')


admin.site.register(Skill, AdminSkill)
admin.site.register(Interest, AdminInterest)
admin.site.register(Association, AdminAssociation)
admin.site.register(Education, AdminEducation)
admin.site.register(EducationNote, AdminEducationNote)
admin.site.register(Project, AdminProject)
admin.site.register(ProjectNote, AdminProjectNote)
admin.site.register(Work, AdminWork)
admin.site.register(WorkNote, AdminWorkNote)
