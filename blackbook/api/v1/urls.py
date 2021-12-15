from django.urls import path, include
from rest_framework import routers
from blackbook.api.v1 import views

router = routers.DefaultRouter()
router.register('company', views.CompanyView, basename='company')

urlpatterns = [
    path('', include(router.urls)),
]
