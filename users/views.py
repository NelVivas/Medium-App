from rest_framework import generics
from rest_framework import viewsets

from users.models import PersonalUser
from users.serializers import UserSerializer

# Create your views here.

#TODO: add viewsets and rest routers
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PersonalUser.objects.all()
    serializer_class = UserSerializer

