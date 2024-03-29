from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product import views

# Initializing the router
router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
