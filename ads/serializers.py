from rest_framework import serializers
from .models import UserClass, Location, Categories, Ads


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    
    class Meta:
        model = UserClass
        fields = '__all__'



class UserCreateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = UserClass.objects.create(**validated_data)

        obj, _ = Location.objects.get_or_create(name=self._location, defaults={'lat': '0', 'lng': '0'})
        user.location = obj

        user.save()
        return user
        
    class Meta:
        model = UserClass
        fields = '__all__'
        
        
class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        obj, _ = Location.objects.get_or_create(name=self._location, defaults={'lat': '0', 'lng': '0'})
        user.location = obj

        user.save()
        return user
        
    class Meta:
        model = UserClass
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClass
        fields = ['id']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
      

class UserForAdSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    
    class Meta:
        model = UserClass
        fields = ['username', 'location']


class AdsSerializer(serializers.ModelSerializer):
    author = UserForAdSerializer(read_only=True)
    
    
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    
    class Meta:
        model = Ads
        fields = '__all__'
