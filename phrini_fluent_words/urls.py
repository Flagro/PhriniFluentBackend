from django.urls import path
from . import views

urlpatterns = [
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
]
