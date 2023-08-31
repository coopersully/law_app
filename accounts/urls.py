from django.urls import path

from accounts import views
from accounts.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', views.account_details, name='logout'),
    path('profile/', views.account_details, name='profile'),
]