from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('all/', views.NotesList.as_view(), name='notes_list'),
    path('<int:pk>', views.NoteDetail.as_view(), name='notes_detail'),

]
