from rest_framework.routers import DefaultRouter

from django.urls import path, include

from articles import views

router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
urlpatterns = router.urls

#urlpatterns = [ path('', include(router.urls) ) ]


