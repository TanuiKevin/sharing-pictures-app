from django.contrib import admin
from .models import Photo

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'uploaded_at')
    ordering = ('-uploaded_at',)
