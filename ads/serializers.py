from rest_framework import serializers
from .models import Ads
from authentication.serializers import UserForAdSerializer



class AdsSerializer(serializers.ModelSerializer):
    author = UserForAdSerializer(read_only=True)
    
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name')
    
    class Meta:
        model = Ads
        fields = '__all__'
