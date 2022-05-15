from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register('', views.LocationViewSet)


urlpatterns = [
   
]

urlpatterns += router.urls
