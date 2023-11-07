from django.urls import path
from . import views

urlpatterns = [
    # CustomUser URLs
    path('users/', views.custom_user_list, name='custom-user-list'),
    path('users/<int:pk>/', views.custom_user_detail, name='custom-user-detail'),
]
