from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from inventory.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
