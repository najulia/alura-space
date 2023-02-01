from django.contrib import admin
from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'legenda')
    list_display_links = ('nome',)
    search_fields = ('nome',)


admin.site.register(Fotografia, FotografiaAdmin)
