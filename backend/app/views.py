
from . models import DataTable
from . serializers import DataTableSerializer
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated


class DataTableViewSet(viewsets.ModelViewSet):
    queryset = DataTable.objects.all()
    serializer_class = DataTableSerializer
    # permission_classes = (IsAuthenticated,)
