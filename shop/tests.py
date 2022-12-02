from django.test import TestCase
from .models import *


class TestCategory(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(id=1)

    def test_name_label(self):
        c = Category.objects.get(id=1)
        field_label = c._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_name_max_length(self):
        c = Category.objects.get(id=1)
        max_length = c._meta.get_field("name").max_length
        self.assertEqual(max_length, 50)


class SwaggerPageTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class ViewEndpointsTest(TestCase):
    def test_category_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/shop/categories/")
        self.assertEqual(response.status_code, 200)

    def test_picture_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/shop/pictures/")
        self.assertEqual(response.status_code, 200)

    def test_products_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/shop/products/")
        self.assertEqual(response.status_code, 200)

    def test_comments_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/shop/comments/")
        self.assertEqual(response.status_code, 200)

    def test_carts_view_url_exists_at_desired_location(self):
        response = self.client.get("/api/shop/carts/")
        self.assertEqual(response.status_code, 200)
