from django.test import TestCase
from django.contrib.auth import get_user_model

from kitchen.models import DishType
from kitchen.forms import (
    DishForm,
    CookCreationForm,
    CookExperienceUpdateForm,
    DishSearchForm,
    CookSearchForm,
    DishTypeSearchForm,
)


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


class CookCreationFormTests(TestCase):
    def test_cook_creation_form_valid(self):
        form_data = {
            "username": "newcook",
            "password1": "strongpassword123",
            "password2": "strongpassword123",
            "years_of_experience": 5,
            "first_name": "Test",
            "last_name": "Cook",
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_creation_form_invalid(self):
        form_data = {
            "username": "newcook",
            "password1": "strongpassword123",
            "password2": "differentpassword",
            "years_of_experience": -5,
            "first_name": "Test",
            "last_name": "Cook",
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class CookExperienceUpdateFormTests(TestCase):
    def setUp(self):
        self.cook = get_user_model().objects.create_user(username="testcook", password="password123",
                                                         years_of_experience=5)

    def test_cook_experience_update_form_valid(self):
        form_data = {"years_of_experience": 10}
        form = CookExperienceUpdateForm(data=form_data, instance=self.cook)
        self.assertTrue(form.is_valid())

    def test_cook_experience_update_form_invalid(self):
        form_data = {"years_of_experience": -10}
        form = CookExperienceUpdateForm(data=form_data, instance=self.cook)
        self.assertFalse(form.is_valid())


class DishSearchFormTests(TestCase):
    def test_dish_search_form_valid(self):
        form_data = {"name": "Test Dish"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_search_form_empty(self):
        form_data = {"name": ""}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class CookSearchFormTests(TestCase):
    def test_cook_search_form_valid(self):
        form_data = {"username": "testcook"}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_cook_search_form_empty(self):
        form_data = {"username": ""}
        form = CookSearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class DishTypeSearchFormTests(TestCase):
    def test_dish_type_search_form_valid(self):
        form_data = {"name": "Main Course"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form_empty(self):
        form_data = {"name": ""}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
