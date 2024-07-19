from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from kitchen.models import (
    Cook,
    Dish,
    DishType
)


def index(request):
    dish_count = Dish.objects.count()
    dish_types_count = DishType.objects.count()
    cooks_count = Cook.objects.count()
    context = {
        "dish_count": dish_count,
        "dish_types_count": dish_types_count,
        "cooks_count": cooks_count
    }
    return render(
        request,
        "kitchen/index.html",
        context=context
    )
