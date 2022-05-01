from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view),
    path('ads/', views.AdsView.as_view()),
    path('cat/', views.CatView.as_view()),
    path('cat/<int:pk>/', views.CatDetailView.as_view()),
    path('ads/<int:pk>/', views.AdDetailView.as_view()),
    # path('save/', views.SaveFromFile.as_view()),
    # path('save_two/', views.SaveFromSecondFile.as_view()),
]
