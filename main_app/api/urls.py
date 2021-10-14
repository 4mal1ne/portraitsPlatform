from django.urls import path

from rest_framework import routers
from .views import WorksViewSet, CommentsViewSet

router = routers.SimpleRouter()
router.register('artworks', WorksViewSet, basename='artworks')
router.register('comments', CommentsViewSet, basename='comments')

urlpatterns = []
urlpatterns += router.urls

