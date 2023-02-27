from django.contrib import admin
from . models import CdcConn, CdcFields, CdcStatus, CdcTables


admin.site.register([CdcConn, CdcFields, CdcStatus, CdcTables])
