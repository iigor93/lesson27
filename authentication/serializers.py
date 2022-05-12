from rest_framework import serializers
from .models import User
from locations.models import Location


class UserSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    
    class Meta:
        model = User
        exclude = ['password', "date_joined"]



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
        user = User.objects.create(**validated_data)

        obj, _ = Location.objects.get_or_create(name=self._location, defaults={'lat': '0', 'lng': '0'})
        user.location = obj

        user.save()
        return user
        
    class Meta:
        model = User
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
        model = User
        fields = '__all__'


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserForAdSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    
    
    class Meta:
        model = User
        fields = ['username', 'location']
