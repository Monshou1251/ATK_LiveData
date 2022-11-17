# from django.urls import path, include
from rest_framework import routers

from .views import DataTableViewSet


router = routers.DefaultRouter()
router.register('datatable', DataTableViewSet)

urlpatterns = router.urls
