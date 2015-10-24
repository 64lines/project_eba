from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _ 
from django.contrib.auth.forms import User

class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=30)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __unicode__(self):
        return self.name

class Lecturer(models.Model):
    full_name = models.CharField(verbose_name=_("Full Name"), max_length=50)
    summary = models.TextField(verbose_name=_("Summary"))

    class Meta:
        verbose_name = _('Lecturer')
        verbose_name_plural = _('Lecturers')

    def __unicode__(self):
        return self.full_name
        
class ConferenceType(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=50)

    class Meta:
        verbose_name = _('Conference type')
        verbose_name_plural = _('Conference types')

    def __unicode__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    
    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    code = models.CharField(verbose_name=_("Code"), max_length=4)
    description = models.TextField(verbose_name=_("Description"))
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    category = models.ForeignKey(Category, verbose_name=_("Category"))
    location = models.ForeignKey(Location, verbose_name=_("Location"))
    details = models.TextField(verbose_name=_("Details"))

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Event')
    
    def __unicode__(self):
        return self.name

class Conference(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    lecturer = models.ForeignKey(Lecturer, verbose_name=_("Lecturer"))
    summary = models.TextField(verbose_name=_("Summary"))
    conference_type = models.ForeignKey(ConferenceType, verbose_name=_("Conference type"))
    location = models.ForeignKey(Location, verbose_name=_("Location"))
    details = models.TextField(verbose_name=_("Details"))
    event = models.ForeignKey(Event, verbose_name=_("Event"))

    class Meta:
        verbose_name = _('Conference')
        verbose_name_plural = _('Conferences')

    def __unicode__(self):
        return self.name

class Attendant(models.Model):
    user = models.ForeignKey(User, verbose_name=_("User"))
    conference = models.ForeignKey(Conference, verbose_name=_("Conference"))

    class Meta:
        verbose_name = _('Attendant')
        verbose_name_plural = _('Attendants')
        
    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

admin.site.register(Category)
admin.site.register(Conference)
admin.site.register(Event)
admin.site.register(ConferenceType)
admin.site.register(Lecturer)
admin.site.register(Attendant)
admin.site.register(Location)
