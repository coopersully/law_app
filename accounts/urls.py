from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from accounts import views
from accounts.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('settings/', views.account_details, name='settings'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)