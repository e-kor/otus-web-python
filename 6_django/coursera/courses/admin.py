from django.contrib import admin

from .models import Course, Lesson


# "@admin.register(Event)j
# 13 class EventAdmin(admin.ModelAdmin):


class LessonInline(admin.TabularInline):
    model = Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    inlines = (LessonInline,)
