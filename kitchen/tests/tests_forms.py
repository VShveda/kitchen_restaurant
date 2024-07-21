from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.forms import (
    DishForm,
    CookCreationForm,
    CookExperienceUpdateForm,
    DishSearchForm,
    CookSearchForm,
    DishTypeSearchForm,
)
from kitchen.models import DishType


class DishFormTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(username="testcook", password="password123")
        self.dishtype = DishType.objects.create(name="Main Course")

    def test_dish_form_valid(self):
        form_data = {
            "name": "Test Dish",
            "description": "Test Description",
            "price": 10.00,
            "dish_type": self.dishtype.id,
            "cooks": [self.cook.id],
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_form_invalid(self):
        form_data = {
            "name": "",
            "description": "Test Description",
            "price": -10.00,
            "dish_type": self.dishtype.id,
            "cooks": [self.cook.id],
        }
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())


