from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.problem_list, name="problems"),
    path('detail/<int:pk>/', views.problem_list, name="detail"),
    path('add/', views.problem_add, name="add"),
    path('update/<int:pk>/', views.problem_update, name="update"),
    path('delete/<int:pk>/', views.problem_delete, name="delete")
]
