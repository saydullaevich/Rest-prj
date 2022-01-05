from rest_framework import serializers
from .models import Category,Post

class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Category
        fields = ('id','name','image')

class CategoryEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('id')

class PostSerializer(serializers.ModelSerializer):
    is_image = serializers.BooleanField()
    is_video = serializers.BooleanField()
    is_audio = serializers.BooleanField()

    class Meta:
        model = Post
        fields = '__all__'

class PostEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id', 'added_at')