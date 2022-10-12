from django.urls import path
from . views import DataTableView


urlpatterns = [
    path('datatable/', DataTableView.as_view(), name='datatable_view')
]