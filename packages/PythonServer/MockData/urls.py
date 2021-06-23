
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from MockData.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
