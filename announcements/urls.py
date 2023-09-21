from django.urls import path

from . import views

urlpatterns = [
    path('', views.announcements, name='announcements'),
    path('new/', views.announcements_new, name='announcements_new'),
]