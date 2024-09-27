from django.urls import path
from .views import index, NoteListView, NoteCreateView, NoteDetailView, NoteUpdateView, NoteDeleteView
urlpatterns = [
    path('', index, name='home'),
    path('my-notes/', NoteListView.as_view(), name='note-list'),
    path('my-notes/create/', NoteCreateView.as_view(), name='note-create'),
    path('my-notes/detail/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('my-notes/update/<int:pk>/', NoteUpdateView.as_view(), name='note-update'),
    path('my-notes/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]