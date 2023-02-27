
from .models import *
from . serializers import CdcConnSerializer, CdcFieldsSerializer, CdcStatusSerializer, CdcTablesSerializer
from rest_framework import viewsets


class CdcConnViewSet(viewsets.ModelViewSet):
    queryset = CdcConn.objects.all()
    serializer_class = CdcConnSerializer


class CdcFieldsViewSet(viewsets.ModelViewSet):
    queryset = CdcFields.objects.all()
    serializer_class = CdcFieldsSerializer


class CdcStatusViewSet(viewsets.ModelViewSet):
    queryset = CdcStatus.objects.all()
    serializer_class = CdcStatusSerializer


class CdcTablesViewSet(viewsets.ModelViewSet):
    queryset = CdcTables.objects.all()
    serializer_class = CdcTablesSerializer
