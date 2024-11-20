from django.shortcuts import get_object_or_404, render

from django.contrib.auth.models import User
from .serializer import UserSerializer, BookSerializer, ReviewSerializer

from django.db import models
from .models import Book,Review

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class BookViewSet(ModelViewSet):
    """
    BookViewSet handles CRUD operations for books.
    - Search books by title, author, or ISBN.
    - Sort books by title, author, average rating, or date added.
    """
     
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend,OrderingFilter, SearchFilter]
    filterset_fields = ['genre']
    search_fields = ['title', 'author', 'isbn']
    ordering_fields = ['title', 'author', 'average_rating', 'date_added']
    ordering = ['title']  

    @action(detail=False, methods=['get'])
    def recommendations(self, request):
        user = request.user
        if not user.is_authenticated:
            return Response({"error": "Authentication required."}, status=401)


        high_rated_genres = Book.objects.values('genre').annotate(avg_rating=models.Avg('reviews__rating')).filter(avg_rating__gte=4).values_list('genre', flat=True)

        recommended_books = Book.objects.filter(genre__in=high_rated_genres).exclude(
            reviews__user=user
        )
        serializer = self.get_serializer(recommended_books, many=True)
        return Response(serializer.data)

class ReviewViewSet(ModelViewSet):
    """
    Viewset for handling CRUD operations on reviews.
    Allows creating, updating, deleting, and listing reviews for books.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer=ReviewSerializer(data=request.data)
        user = User.objects.all()
        if serializer.is_valid():
            user_instance = get_object_or_404(user, id=request.user.id)
            serializer.save(user=user_instance)

        return Response(serializer.data, status=201)

  






