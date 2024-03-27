from django.shortcuts import render
from shop.models import Item

def project_index(request):
    projects = Item.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "index.html", context)