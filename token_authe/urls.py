from django.urls import path
from . import views


urlpatterns = [
    path('', views.myModList.as_view(), name = "myModList"),
    path('person/', views.person_list.as_view(), name = "person_list"),
    path('person/<int:pk>/', views.persondetails.as_view(), name = "persondetails"),
]