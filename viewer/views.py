from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from . import models
from . import forms


class contentListView(generic.ListView):
    model = models.content
    form_class = forms.contentForm


class contentCreateView(generic.CreateView):
    model = models.content
    form_class = forms.contentForm


class contentDetailView(generic.DetailView):
    model = models.content
    form_class = forms.contentForm


class contentUpdateView(generic.UpdateView):
    model = models.content
    form_class = forms.contentForm
    pk_url_kwarg = "pk"


class contentDeleteView(generic.DeleteView):
    model = models.content
    success_url = reverse_lazy("viewer_content_list")

def display(request):
    context = {"content": models.content.objects.all()}
    return render(request, "viewer/content_display.html", context)