from django.urls import path

from rest_framework import routers
from .views import WorksViewSet

router = routers.SimpleRouter()
router.register('artworks', WorksViewSet, basename='artworks')
urlpatterns = []
urlpatterns += router.urls

