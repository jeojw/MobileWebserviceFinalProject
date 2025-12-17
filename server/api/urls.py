from django.urls import path
from .views import upload_image, image_list

urlpatterns = [
    path('upload/', upload_image),
    path('list/', image_list),
]
