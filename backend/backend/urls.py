from django.contrib import admin
from django.urls import path,include

from books.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Book Review API",
        default_version="v1",
        description="API documentation for the Book Review Application",
        contact=openapi.Contact(email="nirujogiprudhvi@gmail.com")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/user/register/',CreateUserView.as_view(),name='register'),
    path('api/token/',TokenObtainPairView.as_view(),name='token'),
    path('api/token/refresh',TokenRefreshView.as_view(),name="refresh"),

    path('api/',include('books.urls')),
    

     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc UI
]
