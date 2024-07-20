from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import DishForm, CookCreationForm, CookExperienceUpdateForm
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


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("kitchen:dish-type-list")


class DishDetailView(generic.DetailView):
    model = Dish


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 3


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 3


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dish__dish_type")


class CookCreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Cook
    form_class = CookCreationForm


class CookExperienceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookExperienceUpdateForm
    success_url = reverse_lazy("kitchen:cook-list")


def cook_assign_to_dish(request, pk):
    cook = Cook.objects.get(id=request.user.id)
    if Dish.objects.get(id=request.user.id):
        cook.dishes.remove(pk)
    else:
        cook.dishes.add(pk)
    return HttpResponseRedirect(reverse_lazy("kitchen:dish-detail", args=[pk]))


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
