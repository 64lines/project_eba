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

class Event(models.Model):
    EVENT_TYPE = (
        ('C', 'Congreso'),
        ('S', 'Seminario'),
        ('T', 'Taller'),
    )

    name = models.CharField(verbose_name=_("Name"), max_length=30)
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    place = models.CharField(verbose_name=_("Place"), max_length=30)
    room = models.CharField(verbose_name=_("Room"), max_length=30)
    event_type = models.CharField(verbose_name=_("Event type"), max_length=1, choices=EVENT_TYPE)
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    conference = models.ManyToManyField(Conference, verbose_name=_("Conference"))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.name

admin.site.register(Category)
admin.site.register(Conference)
admin.site.register(Event)
