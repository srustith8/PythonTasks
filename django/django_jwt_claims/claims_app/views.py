from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated


class ImageViewSet(FlexFieldsModelViewSet):

    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated]
