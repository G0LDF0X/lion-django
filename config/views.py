from django.views.generic import TemplateView, CreateView

# 신규 내용
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomeView(TemplateView):
    template_name = "home.html"

class UserCreateView():
    pass

class UserCreateTV(TemplateView):
    pass