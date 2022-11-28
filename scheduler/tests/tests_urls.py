from django.test import SimpleTestCase
from django.urls import resolve, reverse
from scheduler.views import home

class TestsUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home)