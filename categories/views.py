
from . serializers import CategoriesSerializer
from . models import Categories
from rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
