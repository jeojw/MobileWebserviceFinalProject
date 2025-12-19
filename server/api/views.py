from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ChangeImage
from .serializers import ChangeImageSerializer


@api_view(['POST'])
def upload_image(request):
    serializer = ChangeImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def image_list(request):
    images = ChangeImage.objects.order_by('-created_at')
    serializer = ChangeImageSerializer(images, many=True)
    return Response(serializer.data)