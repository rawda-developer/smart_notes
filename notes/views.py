from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note


class NotesList(ListView):
    model = Note
    context_object_name = 'all_notes'
    template_name = 'notes/all_notes.html'


class NoteDetail(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'notes/note_detail.html'
