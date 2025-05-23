#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
                                        CreateView,
                                        UpdateView,
                                        DeleteView, #new
                                        ) 
from .models import Publication
from django.urls import reverse_lazy #new
from django.contrib.auth.mixins import (
                                        LoginRequiredMixin, #new
                                        UserPassesTestMixin, #new
                                        )

# Create your views here.
class PublicationListView(ListView):
    model = Publication
    template_name = "publications-list.html"

class PublicationDetailView(DetailView):
    model = Publication
    template_name = "publication-detail.html"

class PublicationCreateView(CreateView):
    model = Publication
    template_name = "publication-create.html"
    fields = ['title', 'body']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PublicationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Publication
    template_name = "publication-update.html"
    fields = ['title', 'body']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PublicationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Publication
    template_name = "publication-delete.html"
    success_url = reverse_lazy("publications-list") ###error

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user