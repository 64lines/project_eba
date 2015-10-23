from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _ 

class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=30)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return self.name

class Conference(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=30)
    lecturer = models.CharField(verbose_name=_("Lecturer"), max_length=30)
    abstract = models.TextField(verbose_name=_("Abstract")) 

    class Meta:
        verbose_name = _('Conference')
        verbose_name_plural = _('Conferences')

    def __unicode__(self):
        return self.name

class ActivityType(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=30)

    class Meta:
        verbose_name = _('Activity type')
        verbose_name_plural = _('Activity types')

    def __unicode__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=30)
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    place = models.CharField(verbose_name=_("Place"), max_length=30)
    room = models.CharField(verbose_name=_("Room"), max_length=30)
    activity_type = models.ForeignKey(ActivityType, verbose_name=_("Activity type"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    conference = models.ManyToManyField(Conference, verbose_name=_("Conference"))

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')

    def __unicode__(self):
        return self.name

admin.site.register(Category)
admin.site.register(Conference)
admin.site.register(Activity)
admin.site.register(ActivityType)
