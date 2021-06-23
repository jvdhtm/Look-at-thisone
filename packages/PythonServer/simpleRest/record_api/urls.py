from django.urls import include, path
from rest_framework import routers
# Importing all Views
from . import views
 
router = routers.DefaultRouter()
router.register('NewRecord', views.NewRecordViewSet)
 
# Automatic URL routing
# Login URL for Browsable API Functionality
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]