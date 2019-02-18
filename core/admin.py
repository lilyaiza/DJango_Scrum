from django.contrib import admin
from core.models import *
# Register your models here.

class InlineSprint(admin.TabularInline):
    model = Sprint
    extra = 1

class InlineSpec(admin.TabularInline):
    model = Spec
    extra = 1

class ProjecteAdmin(admin.ModelAdmin):
    inlines = [InlineSprint, InlineSpec]

class SprintAdmin(admin.ModelAdmin):
    list_display = ['projecte','data_inici','data_final','hores']

class SpecsAdmin(admin.ModelAdmin):
    list_display = ['projecte','dificultat','descripcio','hores']

admin.site.register(Projecte,ProjecteAdmin)
admin.site.register(Spec,SpecsAdmin)
admin.site.register(Sprint,SprintAdmin)


