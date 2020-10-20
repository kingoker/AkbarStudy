from django.contrib import admin
from .models import *


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'views', 'price', 'published', 'publish')
    list_display_links = ('name', 'category')
    search_fields = ('name', 'content')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('name', 'publish', 'course')


admin.site.register(Course, CourseAdmin)
admin.site.register(Rubric)
admin.site.register(Lesson, LessonAdmin)

