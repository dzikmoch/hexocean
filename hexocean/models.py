import base64
from io import BytesIO
from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import UserProfile
from PIL import Image as PILImage
from django.core.files.base import ContentFile


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(default=timezone.now, null=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='images/%Y_%m_%d', max_length=100)
    expiry = models.IntegerField(default=300, null=True, blank=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, uploaded: {self.created} by: {self.user}'

    def gen_thumbnails(self) -> None:
        tier = UserProfile.objects.get(user=self.user).tier
        list_heights = tier.thumbnail_size.replace(' ', '').split(',')
        if self.file:
            for new_height in [int(i) for i in list_heights]:
                binary = self.gen_binary(new_height)
                data = ContentFile(base64.b64decode(binary), name='temp.jpg')
                ImageThumbnail.objects.create(file=data, image=self, height=str(new_height))

    def gen_binary(self, custom_height: int = None) -> str:
        data_img = BytesIO()
        with PILImage.open(self.file) as img:
            width, height = img.size
            asp_ratio = height/width
            if custom_height:
                width, height = custom_height/asp_ratio, custom_height

            img.thumbnail((width, height))
            img.save(data_img, format="BMP")
            binary = base64.b64encode(data_img.getvalue()).decode('utf-8')
        return binary

@receiver(post_save, sender=Image)
def thumbnails(sender, instance, created, **kwargs) -> None:
    if created:
        obj = sender.objects.get(pk=instance.pk)
        obj.gen_thumbnails()

class ImageThumbnail(models.Model):
    file = models.ImageField(upload_to='images/%Y_%m_%d/thumbnails', max_length=100, blank=True)
    image = models.ForeignKey(Image, related_name='thumbnails', on_delete=models.CASCADE)
    height = models.CharField(max_length=100, blank=True, null=True)

