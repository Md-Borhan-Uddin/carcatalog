from typing import Any, Dict
from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from core.models import Car

class HomeView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)
        context['recent_list'] = Car.objects.all()[:3]

        return context


class CarDetailView(DetailView):
    model = Car
    template_name = "core/car_detail.html"
    context_object_name = 'car'
    query_pk_and_slug = True
    pk_url_kwarg = 'pk'
    slug_field = 'slug'

    # def get_queryset(self,*args, **kwargs):
    #     data = self.kwargs
    #     return Car.objects.get(id=data.get('pk'),slug=data.get('slug'))
