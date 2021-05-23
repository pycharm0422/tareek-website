from plan import models
from django.contrib import admin
from . import models

admin.site.register(models.Plan)
admin.site.register(models.PlanType)
admin.site.register(models.CanAccess)