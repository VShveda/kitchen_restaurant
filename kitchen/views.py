from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
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


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_types_list"
    template_name = "kitchen/dish_types_list.html"
    paginate_by = 3


class DishTypeCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type_list")


class DishTypeUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish_type_list")

