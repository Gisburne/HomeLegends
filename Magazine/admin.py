__author__ = 'Erik'

from django.contrib import admin
from HomeLegends.Magazine.models import Autors, Rubiks, Stages, Tags, Publications, Pub_meta
#from ckeditor.widgets import CKEditor
#from django.db import models

#class PublicationAdmin(admin.ModelAdmin):
#    formfield_overrides = {
#        models.TextField: {'widget': CKEditor},
#        }

admin.site.register(Autors)
admin.site.register(Rubiks)
admin.site.register(Stages)
admin.site.register(Tags)
admin.site.register(Publications)
admin.site.register(Pub_meta)