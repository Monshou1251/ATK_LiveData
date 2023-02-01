from django.contrib import admin
from . models import CdcConn, CdcFields, CdcStatus, CdcTables


admin.site.register(CdcConn)
admin.site.register(CdcFields)
admin.site.register(CdcStatus)
admin.site.register(CdcTables)
