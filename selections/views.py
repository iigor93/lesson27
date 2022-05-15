from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from selections.models import Selection
from selections.serializers import SelectionSerializer, SelectionCreateUpdateSerializer
from selections.permissions import IsOwner


def main_view(request):
    return JsonResponse({"message": "OK"}, safe=False)


class SelectionView(generics.ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    

class SelectionDetailView(generics.RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes = [IsAuthenticated]
    

class SelectionCreateView(generics.CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateUpdateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateUpdateSerializer
    permission_classes = [IsOwner]
