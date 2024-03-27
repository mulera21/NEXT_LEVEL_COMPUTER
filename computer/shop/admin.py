from django.contrib import admin
from .models import Item


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "more", "description", "info")
    search_field = ("title", "description")


admin.site.register(Item, ProjectAdmin)
