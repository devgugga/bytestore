from rest_framework import viewsets
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer


class CategoryViewSet(viewsets.ViewSet):
    # A simple ViewSet from viewing categories
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data)
