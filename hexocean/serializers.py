from rest_framework import serializers
from .models import Image, ImageThumbnail
from accounts.models import UserProfile
from django.core.validators import FileExtensionValidator
from django.core.files import File
import base64
from datetime import datetime, timedelta
import pytz


class SubImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageThumbnail
        fields = ('height','file')

class ImageSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=None, use_url=True, required=True, validators=[FileExtensionValidator(allowed_extensions=['png','jpg'])])
    name = serializers.CharField()
    expiry = serializers.IntegerField(required=False, min_value=300, max_value=30000)
    thumbnails = SubImageSerializer(many=True, required=False)
    base64 = serializers.SerializerMethodField()

    def get_base64(self, instance: Image) -> str:
        data = 'not available'
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            tier = UserProfile.objects.get(user=user).tier
            if tier.link_expir and isinstance(instance, Image):
                if instance.expiry:
                    timezone = pytz.timezone('Europe/London')
                    time_expiry = instance.created+timedelta(seconds=instance.expiry)
                    time_now = timezone.localize(datetime.now())
                    if time_expiry >= time_now:
                        with open(instance.file.path, 'rb') as file:
                            image = File(file)
                            data = base64.b64encode(image.read())
                    else:
                        data = 'expired'
        return data

    def to_representation(self, instance: Image):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user
            tier = UserProfile.objects.get(user=user).tier
            if not tier.link_orig:
                self.fields.pop('file', None)
            if not tier.link_expir:
                self.fields.pop('expiry', None)
                self.fields.pop('base64', None)

        return super().to_representation(instance)

    class Meta:
        model = Image
        fields = ('name','file','base64','expiry','thumbnails')
