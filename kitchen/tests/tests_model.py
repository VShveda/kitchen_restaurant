from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Cook, Dish


class DishTypeModelTests(TestCase):
    def test_create_dishtype(self):
        dishtype = DishType.objects.create(name="Main Course")
        self.assertEqual(dishtype.name, "Main Course")
        self.assertEqual(str(dishtype), "Main Course")
        self.assertEqual(dishtype._meta.verbose_name, "dishtype")
        self.assertEqual(dishtype._meta.verbose_name_plural, "dishtypes")


class CookModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testcook",
            password="password123",
            first_name="Test",
            last_name="Cook",
            years_of_experience=5
        )

    def test_create_cook(self):
        self.assertEqual(self.user.years_of_experience, 5)
        self.assertEqual(str(self.user), f"testcook ({self.user.first_name} {self.user.last_name})")
        self.assertEqual(self.user._meta.verbose_name, "cook")
        self.assertEqual(self.user._meta.verbose_name_plural, "cooks")


class DishModelTests(TestCase):
    def setUp(self):
        self.dishtype = DishType.objects.create(name="Dessert")
        self.cook = get_user_model().objects.create_user(username="testcook", password="password123")
        self.dish = Dish.objects.create(
            name="Chocolate Cake",
            description="Delicious chocolate cake",
            price=15.99,
            dish_type=self.dishtype
        )
        self.dish.cooks.add(self.cook)

    def test_create_dish(self):
        self.assertEqual(self.dish.name, "Chocolate Cake")
        self.assertEqual(self.dish.description, "Delicious chocolate cake")
        self.assertEqual(self.dish.price, 15.99)
        self.assertEqual(self.dish.dish_type.name, "Dessert")
        self.assertEqual(str(self.dish), "Chocolate Cake")
        self.assertIn(self.cook, self.dish.cooks.all())
        self.assertEqual(self.dish._meta.verbose_name, "dish")
        self.assertEqual(self.dish._meta.verbose_name_plural, "dishes")
