from .serializers import SitesourceSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Sitesource

class SitesourceViewSet(ModelViewSet):
    queryset = Sitesource.objects.all()
    serializer_class = SitesourceSerializer

