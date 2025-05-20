#from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Publication

# Create your views here.
class PublicationListView(ListView):
    model = Publication
    template_name = "publications-list.html"

class PublicationDetailView(DetailView):
    model = Publication
    template_name = "publications-detail.html"