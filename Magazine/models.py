from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Autors(models.Model):
    a_name = models.CharField(max_length=100, verbose_name=_('first name'))
    a_mname = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('midle name'))
    a_lname = models.CharField(max_length=100, verbose_name=_('last name'))
    a_photo = models.ImageField(upload_to='uploads/flatpictures', blank=True, null=True, verbose_name=_('photo'))
    a_birthdate = models.DateField(verbose_name=_('birthday'))
    a_deathdate = models.DateField(blank=True, null=True, verbose_name=_('death day'))
    a_email = models.EmailField(verbose_name=_('e-mail'))
    def __unicode__(self):
        return u'%s %s %s' % (self.a_lname, self.a_name, self.a_mname)
    class Meta:
        verbose_name = _('autor')

class Rubiks(models.Model):
    rubik = models.CharField(max_length=100, verbose_name=_('rubik'))
    def __unicode__(self):
        return self.rubik
    class Meta:
        verbose_name = _('rubik')

class Stages(models.Model):
    stage = models.CharField(max_length=100, verbose_name=_('magazines number'))
    stage_date = models.DateField(verbose_name=_('data magazines number'))
    def __unicode__(self):
        return self.stage
    class Meta:
        verbose_name = _('magazine')

class Tags(models.Model):
    tag = models.CharField(max_length=100, verbose_name=_('tag'))
    def __unicode__(self):
        return self.tag
    class Meta:
        verbose_name = _('tag')

class Publications(models.Model):
    p_title = models.CharField(max_length=250, default='***', verbose_name=_('title'))
    p_text = RichTextField(verbose_name=_('publication'))
    p_date = models.DateField(verbose_name=_('data of publication'))
    aut = models.ManyToManyField(Autors)
    def __unicode__(self):
        return self.p_title
    class Meta:
        verbose_name = _('publication')

class Members(models.Model):
    m_name = models.CharField(max_length=250, verbose_name=_('members name'))
    m_mail = models.EmailField(verbose_name=_('members e-mail'))
    m_format = models.CharField(max_length=3, default='pdf', verbose_name=_('format'))
    def __unicode__(self):
        return self.m_name
    class Meta:
        verbose_name = _('member')

class Pub_meta(models.Model):
    pub = models.ForeignKey(Publications)
    rub = models.ForeignKey(Rubiks)
    sta = models.ForeignKey(Stages)
    tag = models.ManyToManyField(Tags)
    class Meta:
        verbose_name = _('meta information')
