from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Snack


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack

class SnackDetailView(TemplateView):
    template_name = "snack_detail.html"