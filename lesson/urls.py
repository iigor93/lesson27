from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('authentication.urls')),
    path('cat/', include('categories.urls')),
    path('location/', include('locations.urls')),
    path('selection/', include('selections.urls')),
    path('', include("ads.urls")),
    
]
