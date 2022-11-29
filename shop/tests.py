from django.test import TestCase
from .models import *


class TestCategory(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(id=1)

    def test_name_label(self):
        c = Category.objects.get(id=1)
        field_label = c._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        c = Category.objects.get(id=1)
        max_length = c._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)


class SwaggerPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

