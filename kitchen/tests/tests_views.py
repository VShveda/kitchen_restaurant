from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import Dish, DishType, Cook


class IndexViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")

    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")
        self.assertEqual(response.context["dish_count"], Dish.objects.count())
        self.assertEqual(response.context["dish_types_count"], DishType.objects.count())
        self.assertEqual(response.context["cooks_count"], Cook.objects.count())
