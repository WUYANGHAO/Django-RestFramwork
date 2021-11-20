from .models import Sitesource
from rest_framework import serializers

class SitesourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitesource
        fields = '__all__'