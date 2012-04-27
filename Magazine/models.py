from django.db import models
from ckeditor.fields import RichTextField
from photologue.models import ImageModel
from tagging.models import TagManager
from tagging.fields import TagField
from tagging.models import Tag
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Autors(models.Model):
    a_name = models.CharField(max_length=100, verbose_name=_('first name'))
    a_mname = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('midle name'))
    a_lname = models.CharField(max_length=100, verbose_name=_('last name'))
    a_birthdate = models.DateField(verbose_name=_('birthday'))
    a_deathdate = models.DateField(blank=True, null=True, verbose_name=_('death day'))
    a_email = models.EmailField(verbose_name=_('e-mail'))
    def __unicode__(self):
        return u'%s %s %s' % (self.a_lname, self.a_name, self.a_mname)
    class Meta:
        verbose_name = _('autor')
        verbose_name_plural = _('autors')

class AutorPhoto(ImageModel):
    a_photo = models.OneToOneField(Autors, primary_key=True, verbose_name = _('autor photo'))
class Meta:
    verbose_name = _('autor photo')
    verbose_name_plural = _('autor photos')

class Rubiks(models.Model):
    rubik = models.CharField(max_length=100, verbose_name=_('rubik'))
    def __unicode__(self):
        return self.rubik
    class Meta:
        verbose_name = _('rubik')
        verbose_name_plural = _('rubiks')

class Stages(models.Model):
    stage = models.CharField(max_length=100, verbose_name=_('magazines number'))
    stage_date = models.DateField(verbose_name=_('data magazines number'))
    def __unicode__(self):
        return self.stage
    class Meta:
        verbose_name = _('magazine')
        verbose_name_plural = _('magazines')

class Publications(models.Model):
    p_title = models.CharField(max_length=250, default='***', verbose_name=_('title'))
    p_text = RichTextField(verbose_name=_('publication'))
    p_date = models.DateField(verbose_name=_('data of publication'))
    tags = TagField(verbose_name=_('tag'))
#    p_galery = models.OneToOneField('photologue_gallery', blank=True, null=True, verbose_name = _('Publications galery'))
    aut = models.ManyToManyField(Autors, verbose_name=_('autor'))
    rub = models.ForeignKey(Rubiks, verbose_name=_('rubik'))
    sta = models.ForeignKey(Stages, verbose_name=_('magazine'))
    def __unicode__(self):
        return self.p_title
    def get_tag(self):
        return Tag.objects.get_for_object(self)
    def set_tag(self, tag_list):
        return Tag.objects.update_tags(self, tag_list)
    class Meta:
        verbose_name = _('publication')
        verbose_name_plural = _('publications')
