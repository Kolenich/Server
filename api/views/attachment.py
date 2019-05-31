from rest_framework import viewsets
from api.models import Attachment
from api.serializers import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet для модели Customer
    """
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer