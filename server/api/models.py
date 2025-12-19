from django.db import models

class ChangeImage(models.Model):
    change_type = models.CharField(max_length=20)
    image = models.ImageField(upload_to="changes/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.change_type} - {self.created_at}"