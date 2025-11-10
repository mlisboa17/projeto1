from django.contrib import admin
from .models import Transacao

# Register your models here.

@admin.register(Transacao)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor', 'tipo')
    list_filter = ('tipo',)
    search_fields = ('descricao',)
