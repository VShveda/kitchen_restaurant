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


