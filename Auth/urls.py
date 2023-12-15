from django.contrib.auth import views as auth_views
from django.urls import path,include
from . import views


urlpatterns = [
# path("accounts/login/", auth_views.LoginView.as_view()),
    path("accounts/", include("django.contrib.auth.urls")),
    path("change-password/", auth_views.PasswordChangeView.as_view()),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
]