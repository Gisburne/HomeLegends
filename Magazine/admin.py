__author__ = 'Erik'

from django.contrib import admin
#from ckeditor.widgets import CKEditorWidget
from HomeLegends.Magazine.models import Autors, Rubiks, Stages, Publications, AutorPhoto
#from django import forms
#from django.db import models

#class PublicationsAdminForm(forms.ModelForm):
#    content = forms.Textarea(widget = CKEditorWidget())
#    class Meta:
#        model = Publications

class AutorsPhotoAdmin(admin.ModelAdmin):
    list_display = ['admin_thumbnail',]

#class PubGaleryAdmin(admin.ModelAdmin):
#    list_display = ['admin_thumbnail',]

admin.site.register(Autors)
admin.site.register(Rubiks)
admin.site.register(Stages)
admin.site.register(Publications)
admin.site.register(AutorPhoto, AutorsPhotoAdmin)
#admin.site.register(PubGalery)