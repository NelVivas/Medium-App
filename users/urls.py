from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from users import views



router = DefaultRouter()
router.register(r'users',views.UserViewSet )

urlpatterns = [
        
        path('', include(router.urls)),
    
    ]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


