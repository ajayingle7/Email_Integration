from django.urls import path
from .views import signupView,loginView,logoutView,twostepView



urlpatterns = [

    path("signup/", signupView, name="signup"),
    path("login/", loginView, name="login" ),
    path("logout/", logoutView, name="logout" ),
    path("verify/", twostepView, name="verify" )



]