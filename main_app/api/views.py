from rest_framework import viewsets

from .serializers import WorksSerializer
from ..models import Works


class WorksViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer
