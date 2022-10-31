from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.EvDiagnostic)
admin.site.register(models.EngineDiagnostic)
admin.site.register(models.Vehicle)
admin.site.register(models.TroubleCode)
admin.site.register(models.MaintenanceSchedules)
admin.site.register(models.ServiceCenters)
