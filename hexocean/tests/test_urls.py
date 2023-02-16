import pytest
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from hexocean.views import ImageView


class TestImageListUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('ImageList-list')
        assert resolve(url).func.__name__ == ImageView.__name__
