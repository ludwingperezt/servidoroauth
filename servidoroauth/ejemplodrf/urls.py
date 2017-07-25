from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from ejemplodrf import views


router = DefaultRouter()
router.register(r'productos', views.ProductosViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
