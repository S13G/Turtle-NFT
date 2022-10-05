from django.contrib import admin

from setting.models import Settings

# Register your models here.

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request) -> bool:
        return False if self.get_queryset(request).count() == 1 else True
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions