from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import Dish, DishType, Cook


class LoginUserTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="password")
        self.client.login(username="testuser", password="password")


class IndexViewTests(LoginUserTestCase):
    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/index.html")
        self.assertEqual(response.context["dish_count"], Dish.objects.count())
        self.assertEqual(response.context["dish_types_count"], DishType.objects.count())
        self.assertEqual(response.context["cooks_count"], Cook.objects.count())


class DishTypeListViewTests(LoginUserTestCase):
    def test_dish_type_list_view(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "kitchen/dish_types_list.html")
        self.assertEqual(response.context["dish_types_list"].count(), DishType.objects.count())


class DishTypeCreateViewTests(LoginUserTestCase):
    def test_dish_type_create_view(self):
        response = self.client.post(reverse("kitchen:dish-type-create"), {"name": "New DishType"})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("kitchen:dish-type-list"))
        self.assertTrue(DishType.objects.filter(name="New DishType").exists())