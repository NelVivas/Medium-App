from rest_framework.decorators import action
from rest_framework import permissions, viewsets

from articles.serializers import ArticleSerializer
from articles.models import Article
from articles.permissions import IsAuthorOrReadOnly

# Create your views here.

#TODO: add the viewset and rest routers
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [
                permissions.IsAuthenticatedOrReadOnly,
                IsAuthorOrReadOnly
            ]

    @action( detail = True )
    def perform_create(self, serializer):
        serializer.save( author = self.request.user )


