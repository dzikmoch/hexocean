import factory
from django.utils import timezone
from django.contrib.auth.models import User
from accounts.models import UserProfile, Tier
from hexocean.models import Image

class TierFactory(factory.django.DjangoModelFactory):
    name = "x"
    thumbnail_size = "999"
    link_orig = True
    link_expir = True

    class Meta:
        model = Tier


class UserFactory(factory.django.DjangoModelFactory):
    username = "test"
    is_superuser = True
    is_staff = True

    class Meta:
        model = User
        
class UserProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    tier = factory.SubFactory(TierFactory)

    class Meta:
        model = UserProfile
        django_get_or_create = ('user','tier',)
