from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

def profile_photo_upload_to(instance, filename):
    return "profile_photos/user_{0}/{1}".format(instance.id, filename)

# Create your models here.
class User(AbstractUser):
    profile_photo = models.ImageField(upload_to=profile_photo_upload_to, default="profile_photos/default.png")


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    attachments = models.ManyToManyField("FileAttachment", blank=True)
    content = models.TextField()
    parent = models.OneToOneField("self", blank=True, null=True, related_name="response")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class FileAttachment(models.Model):
    file = models.FileField(upload_to="attachments/")
