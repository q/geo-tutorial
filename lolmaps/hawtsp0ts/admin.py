from django.contrib.gis import admin
from lolmaps.hawtsp0ts.models import sp0t

admin.site.register(sp0t, admin.OSMGeoAdmin)
