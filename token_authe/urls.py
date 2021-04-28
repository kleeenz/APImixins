from django.urls import path
from . import views


urlpatterns = [
    path('', views.myModList.as_view(), name = "myModList"),
]