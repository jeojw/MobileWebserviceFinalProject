from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChangeImage
from .serializers import ChangeImageSerializer

API_KEY = "MY_SECRET_KEY"

@api_view(['POST'])
def upload(request):
    key = request.POST.get("key")
    if key != API_KEY:
        return Response({"error": "Unauthorized"}, status=401)

    img = request.FILES.get("image")
    change_type = request.POST.get("type")

    obj = ChangeImage.objects.create(image=img, change_type=change_type)
    return Response({"status": "ok", "id": obj.id})


@api_view(['GET'])
def list_images(request):
    imgs = ChangeImage.objects.order_by("-created_at")
    serializer = ChangeImageSerializer(imgs, many=True)
    return Response(serializer.data)