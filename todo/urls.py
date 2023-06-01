from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', views.TodoView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', views.UserCreate.as_view())
]
