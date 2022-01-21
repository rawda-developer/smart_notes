from django.shortcuts import render
from .models import Note


def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/all_notes.html', {'all_notes': all_notes})
