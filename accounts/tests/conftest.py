from pytest_factoryboy import register
from .factories import UserFactory, TierFactory, UserProfileFactory


register(UserFactory)
register(TierFactory)
register(UserProfileFactory)

