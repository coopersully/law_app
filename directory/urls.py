from django.urls import path

from directory import views

urlpatterns = [
    path('directory/', views.directory, name='directory'),
    path('user/<str:username>/', views.profile, name='view_profile'),
    path('user/<int:user_id>/change', views.change_user_role, name='change_user_role'),
]
