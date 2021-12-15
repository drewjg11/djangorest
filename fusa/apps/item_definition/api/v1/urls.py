from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('item', views.ItemView, basename='item')
router.register('function', views.FunctionView, basename='function')

urlpatterns = [
    path('', include(router.urls)),
    path('item/<int:pk>/function', views.FunctionCreate.as_view(), name='function-create')

]