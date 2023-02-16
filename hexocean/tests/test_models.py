import pytest
from accounts.tests.factories import *
from hexocean.tests.factories import ImageFactory

# pytestmark = pytest.mark.django_db

class TestImageModel:
    user = UserFactory.build()
    tier = TierFactory.build()
    user_profile = UserProfileFactory.build(user=user, tier=tier)

    def test_str_return(self):
        image = ImageFactory.build(user=self.user, name="test-image", created="2023-02-14 12:00:00+00:00")
        assert image.__str__() == "Name: test-image, uploaded: 2023-02-14 12:00:00+00:00 by: test"


