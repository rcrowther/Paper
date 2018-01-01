from django.contrib import admin
from .models import Paper
from . import views


class PaperAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'summary', 'body', 'author')
    list_display = ('title', 'slug')
    show_full_result_count = False
    prepopulated_fields = {"slug": ("title",)}
        
admin.site.register(Paper, PaperAdmin)

