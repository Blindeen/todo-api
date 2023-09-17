from django.urls import path

from todo_api import views

app_name = "todo_api"

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("list/create/", views.CreateListView.as_view(), name="create_list"),
    path("list/<int:id>/delete/", views.DeleteListView.as_view(), name="delete_list"),
    path("list/header/update/", views.SetListHeaderView.as_view(), name="update_header"),
    path("lists/", views.FetchListsView.as_view(), name="display_lists")
]
