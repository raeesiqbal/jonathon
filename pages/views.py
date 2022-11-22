from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from .forms import *


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/home.html")


class InvestorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/investor.html")


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/about.html")


class CareerView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/career.html")


class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/our-services.html")


class DashBoardView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and not request.user.is_superuser:
            return render(request, "pages/dashboard.html")
        if request.user.is_authenticated and request.user.is_superuser:
            return redirect("admin:index")
        return redirect("pages:about")
