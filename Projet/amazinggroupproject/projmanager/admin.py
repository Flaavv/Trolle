from django.contrib import admin 
from .models import Project, Status, Information, Task

admin.site.register(Project)
admin.site.register(Status)
admin.site.register(Information)
admin.site.register(Task)

