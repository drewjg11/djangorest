from rest_framework import serializers
from blackbook.models import Company


class CompanySerializer(serializers.ModelSerializer):
    creator = serializers.StringRelatedField(read_only=True)

    def to_internal_value(self, data):
        if data.get('owner', None) == '':
            data['owner'] = data.get('creator')
        return super(CompanySerializer, self).to_internal_value(data)

    class Meta:
        model = Company
        fields = "__all__"
