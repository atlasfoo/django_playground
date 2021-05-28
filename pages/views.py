from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PageForm
from .models import Page


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, name='dispatch')
class CreatePageView(CreateView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    form_class = PageForm


@method_decorator(staff_member_required, name='dispatch')
class UpdatePageView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class DeletePageView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
