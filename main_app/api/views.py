from rest_framework import viewsets

from .serializers import (
    WorksSerializer,
    CommentsSerializer
)
from ..models import Works, Comments


class WorksViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
