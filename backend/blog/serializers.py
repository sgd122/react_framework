#backend/blog/serializers.py
from rest_framework import serializers
from .models import Blog,Menu

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Blog

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Menu

        