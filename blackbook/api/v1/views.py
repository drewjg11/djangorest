from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from blackbook.models import Company
from blackbook.api.v1.serializers import CompanySerializer


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


    def perform_create(self, serializer):
        creator = self.request.user

        if serializer.validated_data['owner'] == '':
            owner = creator
        else:
            owner = serializer.validated_data['owner']

        serializer.save(creator=creator, owner=owner)
