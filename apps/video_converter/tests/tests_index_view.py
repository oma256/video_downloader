from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def setUp(self) -> None:
        self.valid_video_url = 'https://www.youtube.com/watch?v=-sXw1HJ8SEI'

    def test_form_valid_data(self):
        url = reverse('video_converter:index')
        payload = {
            'url': self.valid_video_url
        }

        r = self.client.post(url, payload)

        self.assertEqual(r.status_code, 301)

    def test_request_get(self):
        url = reverse('video_converter:index')

        r = self.client.get(url)

        self.assertEqual(r.status_code, 200)

    def test_form_invalid_data(self):
        url = reverse('video_converter:index')

        r = self.client.post(url)

        self.assertEqual(r.status_code, 200)
