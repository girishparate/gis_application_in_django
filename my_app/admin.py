from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin, GISModelAdmin
# Register your models here.
from .models import WorldBorder, ModelFields
# @admin.register(WorldBorder)
# class WorldBorderAdmin(OSMGeoAdmin):
#     pass

admin.site.register(WorldBorder, GISModelAdmin)
admin.site.register(ModelFields, GISModelAdmin)