from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, profile_view, profile_edit_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'accounts/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
    path('profile/', profile_view, name = 'profile'),
    path('profile/edit', profile_edit_view, name= 'profile_edit'),
    path(
        'password/change/', 
        auth_views.PasswordChangeView.as_view(
            template_name = 'accounts/password_change.html',
            success_url = '/accounts/profile/'
        ),
        name = 'password_change'
    ),
   
]