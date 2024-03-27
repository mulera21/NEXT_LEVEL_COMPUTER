from django.shortcuts import render
from .models import Item


def project_index(request):
    project = Item.objects.all()

    context = {
        "project": project
    }
    return render(request, "templates/index.html", context)