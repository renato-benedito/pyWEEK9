from django.contrib import admin

# Register your models here.

from .models import Categoria, Flashcard, Desafio, FlashcardDesafio
admin.site.register(Categoria)
admin.site.register(Flashcard)
admin.site.register(Desafio)
admin.site.register(FlashcardDesafio)