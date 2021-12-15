
from django.urls import path, include

urlpatterns = [
    path('', include('fusa.apps.item_definition.api.v1.urls'))
]
