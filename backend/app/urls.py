# from django.urls import path, include
from rest_framework import routers

from .views import CdcConnViewSet, CdcFieldsViewSet, CdcStatusViewSet, CdcTablesViewSet


router = routers.DefaultRouter()
router.register('CdcConn', CdcConnViewSet)
router.register('CdcFields', CdcFieldsViewSet)
router.register('CdcStatus', CdcStatusViewSet)
router.register('CdcTables', CdcTablesViewSet)

urlpatterns = router.urls
