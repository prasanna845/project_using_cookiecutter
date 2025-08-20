from rest_framework import serializers
from .models import Organization, Domain

class OrganizationSerializer(serializers.ModelSerializer):
    domain = serializers.CharField(write_only=True)

    class Meta:
        model = Organization
        fields = ['name', 'schema_name', 'domain']

    def create(self, validated_data):
        domain_name = validated_data.pop('domain')
        tenant = Organization.objects.create(**validated_data)

        Domain.objects.create(
            domain=domain_name,
            tenant=tenant,
            is_primary=True
        )
        return tenant
