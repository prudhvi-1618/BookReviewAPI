from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Book,Review
from django.db import models

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.
    """
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {"password":{"write_only":True}}

    def create(self,validated_data):
        print(validated_data)
        return User.objects.create_user(**validated_data)
    
class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    """
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'genre', 'cover_image_url', 'date_added', 'average_rating']

    def get_average_rating(self, obj):
        return obj.reviews.aggregate(models.Avg('rating'))['rating__avg']
    
class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.
    """
    class Meta:
        model  = Review
        fields = '__all__'
        extra_kwargs = {'user':{"read_only":True}}       
