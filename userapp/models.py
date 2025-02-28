from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_pic = models.ImageField(upload_to="profile_pics/", default="profile_pics/default.jpeg")

    def __str__(self):
        return f"{self.user.username} - Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first

        if self.profile_pic and os.path.exists(self.profile_pic.path):
            img = Image.open(self.profile_pic.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_pic.path, format='JPEG', quality=85)
