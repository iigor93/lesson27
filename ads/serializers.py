from rest_framework import serializers

from ads.models import Ads
from authentication.serializers import UserForAdSerializer


def is_published_false(value):
    if value:
        raise serializers.ValidationError('This field must be False.')


class AdsSerializer(serializers.ModelSerializer):
    author = UserForAdSerializer(read_only=True)
    
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name')
        
    is_published = serializers.BooleanField(default=False, validators=[is_published_false])
    
    class Meta:
        model = Ads
        fields = '__all__'
