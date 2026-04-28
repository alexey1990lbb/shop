from django.test import TestCase, Client
from django.urls import reverse

from .models import Category, Product
from decimal import Decimal


class CatalogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Торты',
            slug='torty'
        )
        self.product = Product.objects.create(
            name='Medovik',
            slug='medovik',
            category=self.category,
            price=Decimal('1000.00'),
            discount_percent=10,
            is_active=True
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, 'Торты')
        self.assertEqual(str(self.category), 'Торты')

    def test_discount_price_calculation(self):
        self.assertEqual(self.product.discount_price, Decimal('900.00'))

    def test_homepage(self):
        response = self.client.get(reverse('shop:home'))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_view(self):
        url = reverse('shop:category-detail', kwargs={'slug': self.category.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Медовик')
