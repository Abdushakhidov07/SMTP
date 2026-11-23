from django.urls import path, include
from .views import *
urlpatterns = [
    path("registration/", registraion, name="registration"),
    path("confirm_email/", confirm_email, name="confirm_email"),
    path("login/", login_user, name="login"),
    path("profile/", show_profile, name="profile")    
]
