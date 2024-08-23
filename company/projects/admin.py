from django.contrib import admin
from .models import Resource,Skill,Task,TaskAssignments,Project
# Register your models here.

admin.site.register(Task)
admin.site.register(TaskAssignments)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Resource)