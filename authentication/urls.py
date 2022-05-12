from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from . import views


urlpatterns = [
  
    path('', views.UsersView.as_view(), name='users'),
    path('create/', views.UsersCreateView.as_view()),
    path('<int:pk>/', views.UsersDetailView.as_view()),
    path('<int:pk>/update/', views.UsersUpdateView.as_view()),
    path('<int:pk>/delete/', views.UsersDeleteView.as_view()),
    
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
]

