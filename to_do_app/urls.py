from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update/<int:pk>/', views.updateTask, name='update'),
    path('edit/<int:pk>/', views.editTask, name='edit'),
    path('delete/<int:pk>/', views.deleteTask, name='delete'),
]
