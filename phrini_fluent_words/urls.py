from django.urls import path
from . import views

urlpatterns = [
    # CustomUser URLs
    path('users/', views.custom_user_list, name='custom-user-list'),
    path('users/<int:pk>/', views.custom_user_detail, name='custom-user-detail'),
    
    # APIKey URLs
    path('api-keys/', views.api_key_list, name='api-key-list'),
    path('api-keys/<int:pk>/', views.api_key_detail, name='api-key-detail'),
    
    # Language URLs
    path('languages/', views.language_list, name='language-list'),
    path('languages/<str:language_tag>/', views.language_detail, name='language-detail'),
    
    # WordGroup URLs
    path('word-groups/', views.word_group_list, name='word-group-list'),
    path('word-groups/<int:pk>/', views.word_group_detail, name='word-group-detail'),
    
    # Word URLs
    path('words/', views.word_list, name='word-list'),
    path('words/<int:pk>/', views.word_detail, name='word-detail'),
    
    # WordDescription URLs
    path('word-descriptions/', views.word_description_list, name='word-description-list'),
    path('word-descriptions/<int:pk>/', views.word_description_detail, name='word-description-detail'),
    
    # Add more paths for other views as needed
]
