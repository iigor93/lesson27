from django.http import JsonResponse
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from ads.serializers import AdsSerializer
from ads.models import Ads
from ads.permissions import IsOwner


def main_view(request):
    return JsonResponse({'status': 'OK'}, safe=False)
        
        
class AdsView(generics.ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    
    def get(self, request, *args, **kwargs):
        
        category_search = request.GET.getlist("cat", None)
        if category_search:
            self.queryset = self.queryset.filter(category__name__in=category_search)
        
        text_search = request.GET.get("text", None)
        if text_search:
            self.queryset = self.queryset.filter(Q(name__icontains=text_search) | Q(description__icontains=text_search))
        
        location_search = request.GET.get("location", None)
        if location_search:
            self.queryset = self.queryset.filter(author__location__name__icontains=location_search)
            
        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_to", None)
        if price_from and price_to:
            self.queryset = self.queryset.filter(price__range=(price_from, price_to))

        return super().get(request, *args, **kwargs)


class AdDetailView(generics.RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]


class AdCreateView(generics.CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]


class AdUpdateView(generics.UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsOwner]

    
class AdDeleteView(generics.DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsOwner]
