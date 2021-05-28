from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PageForm
from .models import Page


class StaffRequiredMixin(object):
    """Use mixin to require staff user logged in
    to access view"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('admin:login')
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class CreatePageView(StaffRequiredMixin, CreateView):
    model = Page
    success_url = reverse_lazy('pages:pages')
    form_class = PageForm


class UpdatePageView(StaffRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class DeletePageView(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
