from django.contrib import admin

from . import models
admin.site.register(models.CustomUser)
admin.site.register(models.Customer)
admin.site.register(models.Performer)
admin.site.register(models.Order)
admin.site.register(models.OrderCategory)
admin.site.register(models.Status)
#
