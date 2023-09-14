from django.urls import path

from todo_api import views

app_name = "todo_api"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login")
]
