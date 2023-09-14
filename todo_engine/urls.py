from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/todo/', include("todo_api.urls", namespace="todo_api"))
]
