from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet, ReviewViewSet




router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'review', ReviewViewSet, basename='review')

urlpatterns = [
    path('',include(router.urls)),

   
]