from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Student, Tutor

admin.site.register(Tutor, UserAdmin)
admin.site.register(Student, UserAdmin)
