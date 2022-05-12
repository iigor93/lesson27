from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Selection
from .serializers import SelectionSerializer, SelectionCreateUpdateSerializer
from .permissions import IsOwner

def main_view(request):
    return JsonResponse({"message": "OK"}, safe=False)


class SelectionView(generics.ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    

class SelectionDetailView(generics.RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes  = [IsAuthenticated]
    

class SelectionCreateView(generics.CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateUpdateSerializer
    permission_classes  = [IsAuthenticated]


class SelectionUpdateView(generics.UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateUpdateSerializer
    permission_classes  = [IsOwner]

    
class SelectionDeleteView(generics.DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer
    permission_classes  = [IsOwner]
