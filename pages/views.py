from django.views.generic import ListView, DetailView

from .models import Page


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
