from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('all/', views.notes_list, name='notes_list'),
    path('<int:pk>', views.note_detail, name='notes_detail'),

]
