from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_documents, name='hub'),
    path('upload/', views.upload_document, name='hub_new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
