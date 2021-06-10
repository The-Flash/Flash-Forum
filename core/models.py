from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone

def profile_photo_upload_to(instance, filename):
    return "profile_photos/user_{0}/{1}".format(instance.id, filename)

# Create your models here.
class User(AbstractUser):
    profile_photo = models.ImageField(upload_to=profile_photo_upload_to, default="profile_photos/default.png")


class Tag(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # User who posted this topic
    tags = models.ManyToManyField("Tag") # Tags associated with a question/topic
    description = models.TextField(blank=True) # Description given to this topic
    created_at = models.DateTimeField(default=timezone.now)
    attachments = models.ManyToManyField("FileAttachment", blank=True) # File attachments

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    attachments = models.ManyToManyField("FileAttachment", blank=True)
    content = models.TextField()
    parent = models.ForeignKey("self", blank=True, null=True, related_name="response", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class FileAttachment(models.Model):
    file = models.FileField(upload_to="attachments/")
