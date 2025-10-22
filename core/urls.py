from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index),
    path('create/', views.add_expense, name='create'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete'),
]