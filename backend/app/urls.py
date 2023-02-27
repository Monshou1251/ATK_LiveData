# from django.urls import path, include
from rest_framework import routers

from .views import CdcConnViewSet, CdcFieldsViewSet, CdcStatusViewSet, CdcTablesViewSet


router = routers.DefaultRouter()
router.register('CdcConn', CdcConnViewSet, basename='cdc_conn')
router.register('CdcFields', CdcFieldsViewSet, basename='cdc_fields')
router.register('CdcStatus', CdcStatusViewSet, basename='cdc_status')
router.register('CdcTables', CdcTablesViewSet, basename='cdc_tables')

urlpatterns = router.urls
