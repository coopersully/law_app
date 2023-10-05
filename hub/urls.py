from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.list_documents, name='hub'),
    path('upload/', views.upload_document, name='hub_new'),
    re_path(r'^serve/(?P<doc_id>[0-9a-f-]+)/$', views.serve_document, name='serve_document'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
