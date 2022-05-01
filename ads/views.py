from django.http import JsonResponse, Http404
from django.views import View
from django.views.generic import DetailView
from .models import Categories, Ads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


def main_view(request):
    return JsonResponse({'status': 'OK'}, safe=False)
        
        
@method_decorator(csrf_exempt, name='dispatch')        
class AdsView(View):
    def get(self, request, *args, **kwargs):
        ads = Ads.objects.all()
        data_to_return = []
        for ad in ads:
            data_to_return.append({'id': ad.id,
                                   'name': ad.name,
                                   'author': ad.author,
                                   'price': ad.price,
                                   'description': ad.description,
                                   'address': ad.address,
                                   'is_published': ad.is_published})
            
        return JsonResponse(data_to_return, safe=False, json_dumps_params={'ensure_ascii': False})
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        all_keys = {'name', 'author', 'price', 'description', 'address', 'is_published'}
        
        if all_keys.issubset(data.keys()):
            ad = Ads()
            
            ad.name = data.get('name')
            ad.author = data.get('author')
            ad.price = data.get('price')
            ad.description = data.get('description')
            ad.address = data.get('address')
            ad.is_published = data.get('is_published')
            ad.save()
        
            return JsonResponse({
                "id": ad.id,
                "name": ad.name,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published}, safe=False)
        return JsonResponse({"error": "wrong data"})
      
        
@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request, *args, **kwargs):
        categories = Categories.objects.all()
        data_to_return = []
        for category in categories:
            data_to_return.append({'id': category.id,
                                   'name': category.name})
            
        return JsonResponse(data_to_return, safe=False, json_dumps_params={'ensure_ascii': False})
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        cat = Categories()
        if data.get('name'):
            cat.name = data.get('name')
            cat.save()
        
            return JsonResponse({
                "id": cat.id,
                "name": cat.name, }, safe=False)
        return JsonResponse({"error": "wrong data"})


class AdDetailView(DetailView):
    model = Ads
    
    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except Http404:
            return JsonResponse({"error": "DoesNotExist"}, safe=False, status=404)
        
        data_to_return = {'id': ad.id,
                          'name': ad.name,
                          'author': ad.author,
                          'price': ad.price,
                          'description': ad.description,
                          'address': ad.address,
                          'is_published': ad.is_published}
        
        return JsonResponse(data_to_return, safe=False)


class CatDetailView(DetailView):
    model = Categories
    
    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except Http404:
            return JsonResponse({"error": "DoesNotExist"}, safe=False, status=404)
        
        data_to_return = {'id': cat.id, 'name': cat.name}
        
        return JsonResponse(data_to_return, safe=False)


class SaveFromSecondFile(View):
    """Save data from Categories file to DB"""
    def get(self, request, *args, **kwargs):
        with open('ads/datasets/categories.csv', 'r', encoding='UTF-8') as f:
            file_read = f.readlines()
        
        for line in file_read[1:]:
            temp_data = line.split(',')
            temp_ads = Categories()
            temp_ads.name = temp_data[1].strip()
            temp_ads.save()
            
        return JsonResponse({"status": "OK"}, safe=False, json_dumps_params={'ensure_ascii': False})


class SaveFromFile(View):
    """Save data from Ads file to DB"""
    def get(self, request, *args, **kwargs):
        with open('ads/datasets/ads.csv', 'r', encoding='UTF-8') as f:
            file_read = f.readlines()
        
        for line in file_read[1:]:
            new_list = []
            i = True
            for item in line:
                if item == '"':
                    i = not i
                if item == ',':
                    if i:
                        new_list.append(';')
                    else:
                        new_list.append(item)
                else:
                    new_list.append(item)
            new_list = ''.join(new_list)
            new_list = new_list.split(';')
            temp_ads = Ads()
             
            temp_ads.name = new_list[1].strip()
            temp_ads.author = new_list[2].strip()
            temp_ads.price = new_list[3].strip()
            temp_ads.description = new_list[4].strip()
            temp_ads.address = new_list[5].strip()
            temp_ads.is_published = True if new_list[6].strip().lower() == 'true' else False
            
            temp_ads.save()
                         
        return JsonResponse({"status": "OK"}, safe=False, json_dumps_params={'ensure_ascii': False})
