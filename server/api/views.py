from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import ChangeImage
from .serializers import ChangeImageSerializer

@api_view(['POST'])
def upload_image(request):
    serializer = ChangeImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "ok"})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def image_list(request):
    images = ChangeImage.objects.order_by('-created_at')
    serializer = ChangeImageSerializer(images, many=True)
    return Response(serializer.data)
