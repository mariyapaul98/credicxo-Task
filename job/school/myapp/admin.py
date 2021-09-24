from django.contrib import admin

# Register your models here.
from .models import login,faculty,student

admin.site.register(login)
admin.site.register(faculty)
admin.site.register(student)
