from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view),
    path('ads/', views.AdsView.as_view(), name='ads'),
    path('ads/create/', views.AdCreateView.as_view()),
    path('ads/<int:pk>/', views.AdDetailView.as_view()),
    path('ads/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ads/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ads/<int:pk>/image/', views.AdImageView.as_view()),
    
    path('cat/', views.CatView.as_view(), name='cat'),
    path('cat/create/', views.CatCreateView.as_view()),
    path('cat/<int:pk>/', views.CatDetailView.as_view()),
    path('cat/<int:pk>/update/', views.CatUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CatDeleteView.as_view()),
    
    path('users/', views.UsersView.as_view(), name='users'),
    path('users/create/', views.UsersCreateView.as_view()),
    path('users/<int:pk>/', views.UsersDetailView.as_view()),
    path('users/<int:pk>/update/', views.UsersUpdateView.as_view()),
    path('users/<int:pk>/delete/', views.UsersDeleteView.as_view()),
    
]
