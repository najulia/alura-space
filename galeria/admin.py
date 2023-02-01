from django.contrib import admin
from galeria.models import Fotografia

class FotografiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'legenda', 'categoria', 'publicada', 'data_publicacao')
    list_display_links = ('nome',)
    search_fields = ('nome', 'categoria')
    list_filter = ('categoria', 'publicada', 'data_publicacao')
    list_editable = ('publicada',)
    list_per_page = 10


admin.site.register(Fotografia, FotografiaAdmin)
