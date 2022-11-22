from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *
from pages.forms import UserLoginForm


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact-us", AboutView.as_view(), name="about"),
    path("investor", InvestorView.as_view(), name="investor"),
    path("careers", CareerView.as_view(), name="career"),
    path("our-services", ServiceView.as_view(), name="service"),
    path("dashboard", DashBoardView.as_view(), name="dashboard"),
    path(
        "login/",
        LoginView.as_view(
            template_name="pages/login.html", authentication_form=UserLoginForm
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
