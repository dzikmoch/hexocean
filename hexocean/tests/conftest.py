from pytest_factoryboy import register
from .factories import ImageFactory, ImageThumbnailFactory


register(ImageFactory)
register(ImageThumbnailFactory)
