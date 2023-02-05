from django.urls import path

from . import views

app_name = "notes"

urlpatterns = [
    path("new1/", views.NoteCreate.as_view(), name="new_note_1"),
    path("new2/", views.note_create, name="new_note_2"),
    path("", views.index, name="index")
]
