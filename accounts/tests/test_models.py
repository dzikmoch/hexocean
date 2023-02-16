import pytest
from .factories import *

pytestmark = pytest.mark.django_db


class TestTierModel:
    def test_str_return(self, tier_factory):
        tier = tier_factory(name="test-tier", thumbnail_size="999")
        assert tier.__str__() == "Name: test-tier; thumbnail sizes: 999"
