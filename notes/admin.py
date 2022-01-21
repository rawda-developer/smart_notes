from django.contrib import admin
from . import models


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


admin.site.register(models.Note, NoteAdmin)
