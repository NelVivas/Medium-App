from rest_framework import viewsets

from categories.models import Category
from categories.serializers import CategorySerializer

# Create your views here.

#TODO: add viewsets and rest routers
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

