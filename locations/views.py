from .models import Location
from .serializers import LocationSerializer
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
