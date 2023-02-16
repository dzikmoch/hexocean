import factory
from django.utils import timezone
from accounts.tests.factories import UserProfileFactory
from hexocean.models import Image, ImageThumbnail
from .factories import *


class ImageFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserProfileFactory)
    created = factory.Faker("date_time", tzinfo=timezone.get_current_timezone())
    name = "x"
    file = factory.django.ImageField()
    expiry = "300"

    class Meta:
        model = Image
        django_get_or_create = ('user',)


class ImageThumbnailFactory(factory.django.DjangoModelFactory):
    file = factory.django.ImageField()
    image = factory.SubFactory(ImageFactory)
    height = "100"

    class Meta:
        model = ImageThumbnail
