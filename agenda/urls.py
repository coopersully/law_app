from django.urls import path

from agenda import views

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('<int:event_id>/', views.event, name='event'),
    path('new/', views.agenda_new, name='agenda_new')
]