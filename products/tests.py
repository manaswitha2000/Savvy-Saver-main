from django.test import TestCase
# from django.db import models
# from django.shortcuts import render, get_object_or_404
from products.models import Product
from products.models import Category

class ProductsTestCase(TestCase):
    print("Testing Product")
    def setUp(self):
        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        # mock_thumbnail = models.ImageField(default='default-product.png', blank=True)
        Category.objects.create(name="testcat1", slug="test_cat_slug_1", thumbnail = "default-product.png")
        cat = Category.objects.get(name="testcat1")
        Product.objects.create(category = cat, name="testProduct1", slug="test_slug_1", url_amazon = "amazon.in", url_flipkart = "flipkart.com", url_jiomart = "jiomart.com", thumbnail = "default-product.png", price_amazon = "10", price_jiomart = "15", price_flipkart = "20")

    def test_products_have_urlamazon(self):
        prod = Product.objects.get(name="testProduct1")
        self.assertEqual(prod.url_amazon, "amazon.in")
        self.assertEqual(prod.url_flipkart, "flipkart.com")
        self.assertEqual(prod.url_jiomart, "jiomart.com")
        print("All urls are present for products 1")

    def test_products_have_correct_price(self):
        prod = Product.objects.get(name="testProduct1")
        self.assertTrue(int(prod.price_amazon) > 0)
        self.assertTrue(int(prod.price_flipkart) > 0)
        self.assertTrue(int(prod.price_jiomart) > 0)
        print("All prices are valid for products 1")

# Create your tests here.
