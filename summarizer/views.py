from rest_framework.viewsets import ModelViewSet
from summarizer.models import Photo
from summarizer.serializers import PhotoSerializer


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

