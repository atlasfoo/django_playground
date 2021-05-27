from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .models import Page


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class CreatePageView(CreateView):
    model = Page
    fields = ['title', 'content', 'order', ]

    success_url = reverse_lazy('pages:pages')
