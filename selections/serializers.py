from rest_framework import serializers

from selections.models import Selection


class SelectionSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    
    ads = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='name')
    
    class Meta:
        model = Selection
        fields = ['id', 'name', 'owner', 'ads']
        

class SelectionCreateUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Selection
        fields = '__all__'
