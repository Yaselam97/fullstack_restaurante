from django.contrib import admin
from .models import Dish
from .models import ContactMessage

admin.site.register(Dish)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'timestamp')  # Mostra nome, email e data
    readonly_fields = ('name', 'email', 'message', 'timestamp')  # Rendi i campi di sola lettura
    ordering = ('-timestamp',)  # Ordina dal più recente

    # Disabilita l'aggiunta, modifica ed eliminazione
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False