from django.shortcuts import render
from .models import Note
from .forms import NoteForm

# Create your views here.

def notes_list(request):
    return render(request, "notes/notes_list.html", {"notes": notes})

def notes_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)

    return render(request, "notes/notes_detail.html", {"note": note})

def notes_create(request, pk):
    if request.method == "GET":
        form = NoteForm()

    else:
        form = NoteForm(data=request.POST)

    return render(request, "notes/notes_create.html", {'form': form})

def notes_update(request, pk):
    pass

def notes_delete(request, pk):
    pass

