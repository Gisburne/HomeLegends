__author__ = 'Erik'

from django.contrib import admin
from Magazine.models import *


class AutorPhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_taken', 'date_added', 'is_public', 'tags', 'view_count', 'admin_thumbnail')
    list_filter = ['date_added', 'is_public']
    search_fields = ['title', 'caption']
    list_per_page = 10
    prepopulated_fields = {'title_slug': ('title',)}

class PubGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added', 'photo_count', 'is_public')
    list_filter = ['date_added', 'is_public']
    date_hierarchy = 'date_added'
    prepopulated_fields = {'title_slug': ('title',)}
    filter_horizontal = ('photos',)

class PubAdmin(admin.ModelAdmin):
    filter_horizontal = ('aut',)

admin.site.register(Autors)
admin.site.register(Rubiks)
admin.site.register(Stages)
admin.site.register(Publications, PubAdmin)
admin.site.register(AutorPhoto, AutorPhotoAdmin)
admin.site.register(Pub_gallery, PubGalleryAdmin)