from django.contrib import admin
from django.urls import path, include

from django.shortcuts import render

def home(request):
    words = "solomon"
    return render(request, "index.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/v1/", include("main.urls")),
    path('',home)

]
