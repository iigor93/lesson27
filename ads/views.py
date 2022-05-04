from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse, Http404
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Categories, Ads, UserClass, Location
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


def main_view(request):
    return JsonResponse({'status': 'OK'}, safe=False)
        
          
class AdsView(ListView):
    model = Ads
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        
        ads = self.object_list.order_by("-price")
        
        paginator = Paginator(ads, settings.TOTAL_ON_PAGE)
        page_number = int(request.GET.get('page', 1)) if int(request.GET.get('page', 1)) in paginator.page_range else 1
        
        data_to_return = []
        for ad in paginator.page(page_number).object_list:
            data_to_return.append({'id': ad.id,
                                   'name': ad.name,
                                   'author': ad.author_id,
                                   'price': ad.price,
                                   'description': ad.description,
                                   'is_published': ad.is_published,
                                   'category': ad.category_id,
                                   'image': ad.image.url if ad.image else 'No image'})
                                   
        dict_return = {"num_pages": paginator.num_pages,
                       "total": paginator.count,
                       "current_page": page_number,
                       "items": data_to_return}
            
        return JsonResponse(dict_return, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        ads_data = json.loads(request.body)
        all_keys = {'name', 'author', 'price', 'description', 'is_published', 'category'}
        
        if all_keys.issubset(ads_data.keys()):
            ad = Ads.objects.create(
                name=ads_data['name'],
                author_id = ads_data['author'],
                price = ads_data['price'],
                description = ads_data['description'],
                is_published = ads_data['is_published'],
                category_id = ads_data['category']
                )
                
            ad.save()
            return JsonResponse({
                    "id": ad.id,
                    "name": ad.name,
                    "author": ad.author_id,
                    "price": ad.price,
                    "description": ad.description,
                    "is_published": ad.is_published,
                    "category": ad.category_id}, safe=False)
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
                          'author': ad.author_id,
                          'price': ad.price,
                          'description': ad.description,
                          'category': ad.category_id,
                          'is_published': ad.is_published,
                          'image': ad.image.url if ad.image else 'No image'
                          }
        
        return JsonResponse(data_to_return, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = Ads
    fields = ["logo"]

    def post(self, request, *args, **kwargs):
        ad = self.get_object()

        ad.image = request.FILES["logo"]
        ad.save()

        data_to_return = {'id': ad.id,
                          'name': ad.name,
                          'author': ad.author_id,
                          'price': ad.price,
                          'description': ad.description,
                          'category': ad.category_id,
                          'is_published': ad.is_published,
                          'image': ad.image.url if ad.image else 'No image'
                          }
        
        return JsonResponse(data_to_return, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ads
    fields = ['name', 'author', 'price', 'description', 'is_published', 'category']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        ads_data = json.loads(request.body)
        
        self.object.name = ads_data['name']
        self.object.author_id = ads_data['author']
        self.object.price = ads_data['price']
        self.object.description = ads_data['description']
        self.object.is_published = ads_data['is_published']
        self.object.category_id = ads_data['category']
        
        self.object.save()
        
        return JsonResponse({
                "id": self.object.id,
                "name": self.object.name,
                "author": self.object.author_id,
                "price": self.object.price,
                "description": self.object.description,
                "is_published": self.object.is_published,
                "category": self.object.category_id}, safe=False)   
    

@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ads
    success_url = "ads"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
      
        
@method_decorator(csrf_exempt, name='dispatch')
class CatView(ListView):
    model = Categories
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        
        cat = self.object_list.order_by("name")
        
        paginator = Paginator(cat, settings.TOTAL_ON_PAGE)
        page_number = int(request.GET.get('page', 1)) if int(request.GET.get('page', 1)) in paginator.page_range else 1
        
        data_to_return = []
        for category_ in paginator.page(page_number).object_list:
            data_to_return.append({'id': category_.id,
                                   'name': category_.name})
                                   
        dict_return = {"num_pages": paginator.num_pages,
                       "total": paginator.count,
                       "current_page": page_number,
                       "items": data_to_return}
            
        return JsonResponse(dict_return, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Categories
    fields = ['name']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        cat_data = json.loads(request.body)
        all_keys = {'name'}
        
        if all_keys.issubset(cat_data.keys()):
            cat = Categories.objects.create(
                name=cat_data['name']
                )
                
            cat.save()
            return JsonResponse({
                    "id": cat.id,
                    "name": cat.name}, safe=False)
        return JsonResponse({"error": "wrong data"})


class CatDetailView(DetailView):
    model = Categories
    
    def get(self, request, *args, **kwargs):
        try:
            cat = self.get_object()
        except Http404:
            return JsonResponse({"error": "DoesNotExist"}, safe=False, status=404)
        
        data_to_return = {'id': cat.id, 'name': cat.name}
        
        return JsonResponse(data_to_return, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CatUpdateView(UpdateView):
    model = Categories
    fields = ['name']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        cat_data = json.loads(request.body)
        
        self.object.name = cat_data['name']
        
        self.object.save()
        
        return JsonResponse({
                "id": self.object.id,
                "name": self.object.name}, safe=False)   


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteView(DeleteView):
    model = Categories
    success_url = "cat"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class UsersView(ListView):
    model = UserClass
    
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        
        users = self.object_list.select_related('location')
        
        paginator = Paginator(users, settings.TOTAL_ON_PAGE)
        page_number = int(request.GET.get('page', 1)) if int(request.GET.get('page', 1)) in paginator.page_range else 1
        
        data_to_return = []
        
        for user in paginator.page(page_number).object_list:
            data_to_return.append({'id': user.id,
                                   'username': user.username,
                                   'first_name': user.first_name,
                                   'last_name': user.last_name,
                                   'role': user.role,
                                   'age': user.age,
                                   'location': user.location.name,
                                   'all ads for user': user.ads_set.filter(is_published__exact=True).count()})
                                   
        dict_return = {"num_pages": paginator.num_pages,
                       "total": paginator.count,
                       "current_page": page_number,
                       "items": data_to_return}
            
        return JsonResponse(dict_return, safe=False, json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class UsersCreateView(CreateView):
    model = UserClass
    fields = ['username', 'first_name', 'last_name', 'password', 'role', 'age', 'location']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        user_data = json.loads(request.body)
        all_keys = {'username', 'first_name', 'last_name', 'password', 'role', 'age', 'location'}
        
        if all_keys.issubset(user_data.keys()):
            user = UserClass.objects.create(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password=user_data['password'],
                role=user_data['role'],
                age=user_data['age']                
                )
            
            location_, _ = Location.objects.get_or_create(name=user_data['location'], defaults={'lat': '0', 'lng': '0'})
            user.location = location_
                
            user.save()
            return JsonResponse({
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "age": user.age,
                    "location": user.location.name
                    
                    }, safe=False)
        return JsonResponse({"error": "wrong data"})


class UsersDetailView(DetailView):
    model = UserClass
    
    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except Http404:
            return JsonResponse({"error": "DoesNotExist"}, safe=False, status=404)
        
        data_to_return = {'id': user.id, 
                          'username': user.username,
                          'first_name': user.first_name,
                          'last_name': user.last_name,
                          'role': user.role,
                          'age': user.age,
                          'location': user.location.name,
                          'all ads for user': user.ads_set.filter(is_published__exact=True).count()}
        
        return JsonResponse(data_to_return, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UsersUpdateView(UpdateView):
    model = UserClass
    fields = ['username', 'first_name', 'last_name', 'password', 'role', 'age', 'location']
    
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        
        user_data = json.loads(request.body)
        all_keys = {'username', 'first_name', 'last_name', 'password', 'role', 'age', 'location'}
        
        if all_keys.issubset(user_data.keys()):
            self.object.username=user_data['username']
            self.object.first_name=user_data['first_name']
            self.object.last_name=user_data['last_name']
            self.object.password=user_data['password']
            self.object.role=user_data['role']
            self.object.age=user_data['age']                
                
            
            location_, _ = Location.objects.get_or_create(name=user_data['location'], defaults={'lat': '0', 'lng': '0'})
            self.object.location = location_

            self.object.save()
        
            return JsonResponse({
                    "id": self.object.id,
                    "username": self.object.username,
                    "first_name": self.object.first_name,
                    "last_name": self.object.last_name,
                    "role": self.object.role,
                    "age": self.object.age,
                    "location": self.object.location.name
                    
                    }, safe=False)
        return JsonResponse({"error": "wrong data"})


@method_decorator(csrf_exempt, name='dispatch')
class UsersDeleteView(DeleteView):
    model = UserClass
    success_url = "users"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
