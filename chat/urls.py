from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat, name='chat'),
    path('<str:room_name>/past_messages/', views.get_past_messages, name='get_past_messages'),
]