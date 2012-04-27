from django.db import models
from ckeditor.fields import RichTextField
from photologue.models import ImageModel, Gallery
import tagging
from tagging.fields import TagField
from tagging.models import Tag
from tagging.utils import parse_tag_input
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Autors(models.Model):
    a_name = models.CharField(max_length=100, verbose_name=_('first name'))
    a_mname = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('midle name'))
    a_lname = models.CharField(max_length=100, verbose_name=_('last name'))
#    a_photo = models.ImageField(upload_to='uploads/flatpictures', blank=True, null=True, verbose_name=_('photo'))
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

#class Tags(models.Model):
#    tag = models.CharField(max_length=100, verbose_name=_('tag'))
#    def __unicode__(self):
#        return self.tag
#    class Meta:
#        verbose_name = _('tag')
#        verbose_name_plural = _('tags')

class Publications(models.Model):
    p_title = models.CharField(max_length=250, default='***', verbose_name=_('title'))
    p_text = RichTextField(verbose_name=_('publication'))
    p_date = models.DateField(verbose_name=_('data of publication'))
    aut = models.ManyToManyField(Autors)
    def __unicode__(self):
        return self.p_title
    class Meta:
        verbose_name = _('publication')
        verbose_name_plural = _('publications')

class PubGalery(Gallery):
    p_galery = models.OneToOneField(Publications, primary_key=True, verbose_name = _('Publications galery'))
    class Meta:
        verbose_name = _('Publications galery')
        verbose_name_plural = _('Publications galerys')

class Members(models.Model):
    m_name = models.CharField(max_length=250, verbose_name=_('members name'))
    m_mail = models.EmailField(verbose_name=_('members e-mail'))
    m_format = models.CharField(max_length=3, default='pdf', verbose_name=_('format'))
    def __unicode__(self):
        return self.m_name
    class Meta:
        verbose_name = _('member')
        verbose_name_plural = _('members')

class Pub_meta(models.Model):
    pub = models.ForeignKey(Publications)
    rub = models.ForeignKey(Rubiks)
    sta = models.ForeignKey(Stages)
#    tag = models.ManyToManyField(Tags)
    tags = TagField(verbose_name = 'tag')
    def get_tag(self):
        return Tag.objects.get_for_object(self)
    def __unicode__(self):
        return Publications.p_title
    class Meta:
        verbose_name = _('meta information')
        verbose_name_plural = _('meta informations')
