# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.urls import reverse


class SearchIndexViewTestCase(TestCase):
    """Test the app's main search functionality."""

    def setUp(self, *args, **kwargs):
        self.client = Client()
        self.url = reverse('search:index')

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        return True
