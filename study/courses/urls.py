from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('courses/', get_courses, name='courses'),
    path('course/<int:course_id>/', get_lessons, name='lessons'),
    path('lesson/<int:lesson_id>/<int:course_id>', show_lesson, name='lesson'),
    path('users/', include('users.urls'), name='users'),
]