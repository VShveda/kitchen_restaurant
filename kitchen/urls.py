from django.contrib.auth import views
from django.urls import path

from kitchen.views import index


urlpatterns = [
    path("", index, name="index"),
    path("login/", views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(next_page="login"), name="logout"),
]

app_name = "kitchen"
