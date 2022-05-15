from django.urls import path

from . import views


urlpatterns = [
    path('main', views.main_view),
    path('', views.SelectionView.as_view()),
    path('create/', views.SelectionCreateView.as_view()),
    path('<int:pk>/', views.SelectionDetailView.as_view()),
    path('<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', views.SelectionUpdateView.as_view()),

]
