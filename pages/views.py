from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Page


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class CreatePageView(CreateView):
    model = Page
    fields = ['title', 'content', 'order', ]
    success_url = reverse_lazy('pages:pages')


class UpdatePageView(UpdateView):
    model = Page
    fields = ['title', 'content', 'order', ]
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class DeletePageView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
