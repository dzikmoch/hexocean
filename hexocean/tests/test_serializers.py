import pytest
import factory
from accounts.tests.factories import UserFactory, UserProfileFactory, TierFactory
from hexocean.tests.factories import ImageFactory, ImageThumbnailFactory
from hexocean.serializers import ImageSerializer, SubImageSerializer

pytestmark = pytest.mark.django_db


class TestSubImageSerializer:
    user = UserFactory.build()
    tier = TierFactory.build()
    user_profile = UserProfileFactory.build(user=user, tier=tier)
    image = ImageFactory.build(user=user, expiry=300, file=None)

    def test_serialize_model(self):
        image_thumbnail = ImageThumbnailFactory.build(image=self.image)
        serializer = SubImageSerializer(image_thumbnail)
        assert serializer.data

    def test_serialized_data(self, mocker):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=ImageThumbnailFactory,
            image=self.image
        )

        serializer = SubImageSerializer(data=valid_serialized_data)
        assert serializer.is_valid()
        assert serializer.errors == {}


class TestImageSerializer:
    user = UserFactory.build()
    tier = TierFactory.build()
    user_profile = UserProfileFactory.build(user=user, tier=tier)

    def test_serialize_model(self):
        image = ImageFactory.build(pk=1,user=self.user, expiry=300, file=None)
        thumbnails = ImageThumbnailFactory.build(image=image)
        expected_serialized_data = {
            'thumbnails': [],
            'name': image.name,
            'file': image.file,
            'base64': 'not available',
            'expiry': image.expiry,
        }

        serializer = ImageSerializer(image)
        assert serializer.data == expected_serialized_data

    def test_serialized_data(self, mocker):
        image = ImageFactory.build(user=self.user, expiry=300)
        valid_serialized_data = {
            'user': image.user,
            'created': image.created,
            'name': image.name,
            'file': image.file,
            'expiry': image.expiry,
        }

        serializer = ImageSerializer(data=valid_serialized_data)
        assert serializer.is_valid(raise_exception=True)
        assert serializer.errors == {}