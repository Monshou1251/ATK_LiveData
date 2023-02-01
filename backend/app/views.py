
from . models import *
from . serializers import CdcConnSerializer, CdcFieldsSerializer, CdcStatusSerializer, CdcTablesSerializer
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated


class CdcConnViewSet(viewsets.ModelViewSet):
    queryset = CdcConn.objects.all()
    serializer_class = CdcConnSerializer
    # permission_classes = (IsAuthenticated,)


class CdcFieldsViewSet(viewsets.ModelViewSet):
    queryset = CdcFields.objects.all()
    serializer_class = CdcFieldsSerializer
    # permission_classes = (IsAuthenticated,)


class CdcStatusViewSet(viewsets.ModelViewSet):
    queryset = CdcStatus.objects.all()
    serializer_class = CdcStatusSerializer
    # permission_classes = (IsAuthenticated,)


class CdcTablesViewSet(viewsets.ModelViewSet):
    queryset = CdcTables.objects.all()
    serializer_class = CdcTablesSerializer
    # permission_classes = (IsAuthenticated,)
