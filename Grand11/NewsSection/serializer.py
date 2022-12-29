from rest_framework import serializers
from .models import *



class Serializer_Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        

class Serializer_SubCategory(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.name')
    class Meta:
        model = SubCategory
        fields = '__all__'
        
    
class Serializer_News(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='Category.name')
    subcategoy_name=serializers.ReadOnlyField(source='SubCategory.name')
    class Meta:
        model=News
        fields='__all__'    
    
class Serializer_Videonews(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='Category.name')
    subcategoy_name=serializers.ReadOnlyField(source='SubCategory.name')
    class Meta:
        model=VideoNews
        fields='__all__'    
    
    
