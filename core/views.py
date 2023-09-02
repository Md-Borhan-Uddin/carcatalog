from typing import Any, Dict
from django.utils.text import slugify
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView,ListView

from core.forms import CarCreateForm

from core.models import Car

class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['recent_list'] = Car.objects.all()[:3]

        return context


class CarListView(ListView):
    model = Car
    template_name = "core/car_list.html"
    context_object_name = 'cars'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_per_page'] = self.paginate_by
        return context

    


class CarDetailView(DetailView):
    model = Car
    template_name = "core/car_detail.html"
    context_object_name = 'car'
    query_pk_and_slug = True
    pk_url_kwarg = 'pk'
    slug_field = 'slug'


class CarCreateView(CreateView):
    model = Car
    template_name = "core/create_car.html"
    form_class = CarCreateForm


    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        print(form.instance)
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.title)
        car = form.save()
        return super().form_invalid(form)
