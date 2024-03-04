from django.contrib import admin

# Register your models here.

from database import models

admin.site.register(models.NodeInfo)
admin.site.register(models.Link)
admin.site.register(models.User)
admin.site.register(models.Favourite)
