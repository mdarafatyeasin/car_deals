from django.urls import path
from . import views 


urlpatterns = [
    path('user_registration',views.UserRegistration, name="user_registration"),
    path('login',views.UserLogin, name="user_login"),
    path('logout',views.Logout, name="logout"),
    path('user_profile',views.Profile, name="user_profile"),
    path('edit_profile',views.editProfile, name="edit_profile"),
    path('change_password',views.changePassword, name="change_password"),
]
