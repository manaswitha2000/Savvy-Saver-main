from django.test import TestCase
# Create your tests here.
from basket.models import Basket

#
#
class BasketTestCase(TestCase):
    print("Testing Basket")
    def setUp(self):
        # created_at = models.DateTimeField(auto_now_add=True)
        # updated_at = models.DateTimeField(auto_now=True)
        Basket.objects.create(total_amazon = 10, total_flipkart = 20, total_jiomart = 30)

    def test_basket_sum(self):
        basket = Basket.objects.get(total_amazon = 10)
        self.assertTrue(int(basket.total_amazon) > 0)
        self.assertTrue(int(basket.total_flipkart) > 0)
        self.assertTrue(int(basket.total_jiomart) > 0)
        print("All prices are valid for bastet")
