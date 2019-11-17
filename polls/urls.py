from django.urls import path, include
from . import views

app_name = 'name'

urlpatterns = [
    path('', views.Get_name.as_view(), name="name"),
    path('result/', views.result, name="result")
]