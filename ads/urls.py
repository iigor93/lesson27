from django.urls import path
from . import views


urlpatterns = [
    path('', views.main_view),
    path('ads/', views.AdsView.as_view(), name='ads'),
    path('ads/create/', views.AdCreateView.as_view()),
    path('ads/<int:pk>/', views.AdDetailView.as_view()),
    path('ads/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ads/<int:pk>/delete/', views.AdDeleteView.as_view()),
    
]

