from django.shortcuts import render
from .models import Note


def notes_list(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/all_notes.html', {'all_notes': all_notes})


def note_detail(request, pk):
    try:
        note = Note.objects.get(pk=pk)
    except Note.DoesNotExist:
        return render(request, 'notes/404.html', {})
    return render(request, 'notes/note_detail.html', {'note': note})
