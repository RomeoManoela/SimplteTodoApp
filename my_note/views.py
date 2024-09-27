
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Note
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'my_note/index.html')


class NoteListView(ListView):
    model = Note
    context_object_name = 'notes'

    def get_queryset(self):
        query = super().get_queryset()
        title = self.request.GET.get('title')
        if title:
            query = query.filter(title__icontains=title)
        return query




class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note-list')


class NoteDetailView(DetailView):
    model = Note
    context_object_name = 'note'
    template_name = 'my_note/note_detail.html'


class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    success_url = reverse_lazy('note-list')


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')


