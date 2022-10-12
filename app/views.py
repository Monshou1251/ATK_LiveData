from rest_framework.response import Response
from rest_framework import generics
from . models import DataTable
from . serializers import DataTableSerializer


class DataTableView(generics.RetrieveAPIView):
    queryset = DataTable.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = DataTableSerializer(queryset, many=True)
        return Response(serializer.data)

# class DataTableViewSet(viewsets.ModelViewSet):
#     queryset = DataTable.objects.all().order_by('-created_at')
#     serializer_class = DataTableSerializer


