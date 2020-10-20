from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def index(request):
    return render(request, 'courses/index.html')


def get_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'courses/courses.html', context)


def get_lessons(request, course_id):
    course = Course.objects.get(id=course_id)
    lessons = Lesson.objects.filter(course=course_id)
    context = {'course': course, 'lessons': lessons}
    return render(request, 'courses/course_page.html', context)


def show_lesson(request, lesson_id, course_id):
    courses = Course.objects.all()
    lesson = Lesson.objects.get(id=lesson_id)
    lessons = Lesson.objects.filter(course=course_id)
    context = {'lesson': lesson, 'lessons': lessons, 'courses': courses}
    return render(request, 'courses/lesson_page.html', context)

