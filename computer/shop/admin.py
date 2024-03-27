from django.contrib import admin
from .models import Item


class ProjectAdmin(admin.ModelAdmin):
    pass


admin.site.register(Item, ProjectAdmin)
