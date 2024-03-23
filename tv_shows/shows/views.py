from .models import Show
from rest_framework import viewsets, permissions
from .serializers import ShowSerializer

# Create your views here.
class ShowViews(viewsets.ModelViewSet):
    queryset=Show.objects.all()
    serializer_class=ShowSerializer
    permission_classes=[permissions.AllowAny]