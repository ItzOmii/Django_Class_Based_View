from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from first_app import models
from django.urls import reverse_lazy


class IndexView(ListView):
    context_object_name='musician_list'
    model=models.Musician
    template_name='first_app/index.html'

class MusicianDetail(DetailView):
    context_object_name='musician'
    model=models.Musician
    template_name='first_app/musician_detail.html'

class AddMusician(CreateView):
    fields=('first_name','last_name','instrument')
    model=models.Musician
    template_name='first_app/musician_form.html'


class UpdateMusician(UpdateView):
    fields=('first_name','last_name','instrument')
    model=models.Musician

class DeleteMusician(DeleteView):
        context_object_name='musician'
        model=models.Musician
        success_url=reverse_lazy('first_app:index')
        template_name='first_app/delete_musician.html'
