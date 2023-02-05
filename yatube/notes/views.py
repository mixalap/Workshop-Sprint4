from django.views.generic.edit import CreateView

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import NoteForm
from .models import Note

def index(request):
    notes = Note.objects.order_by("-pub_date").filter(publish=True)
    context = {
        "notes": notes,
    }
    return render(request, "notes/index.html", context)

class NoteCreate(CreateView): #Создаём свой класс, наследуем его от CreateView
    # С какой формой будет работать этот класс
    form_class = NoteForm
    # Какой шабон применить для отображения веб-формы
    template_name = 'notes/new_note.html'
    # Куда переадресовать пользователя после того, как он отправит форму
    success_url = reverse_lazy('notes:index')

def note_create(request):
    form = NoteForm(request.POST or None)
    if not request.method == "POST":
        return render(request, "notes/new_note_2.html", {"form": form})

    if not form.is_valid():
        return render(request, "notes/new_note_2.html", {"form": form})
    
    post = form.save(commit=False)
    post.text = 'Mod text: {}'.format(post.name) 
    post.save()

    return redirect("notes:index")
