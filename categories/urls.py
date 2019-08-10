from rest_framework.routers import DefaultRouter

from django.urls import path, include

from categories import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


