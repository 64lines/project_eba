from django.db import models
from django.contrib import admin

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __unicode__(self):
        return self.name

class Conference(models.Model):
    name = models.CharField(max_length=30)
    lecturer = models.CharField(max_length=30)
    abstract = models.TextField() 

    class Meta:
        verbose_name = 'Conferencia'
        verbose_name_plural = 'Conferencias'

    def __unicode__(self):
        return self.name

class Event(models.Model):
    EVENT_TYPE = (
        ('C', 'Congreso'),
        ('S', 'Seminario'),
        ('T', 'Taller'),
    )

    name = models.CharField("nombre", max_length=30)
    start_date = models.DateTimeField("fecha de inicio")
    end_date = models.DateTimeField("fecha de finalizacion")
    place = models.CharField("lugar", max_length=30)
    room = models.CharField("salon", max_length=30)
    event_type = models.CharField("tipo de evento", max_length=1, choices=EVENT_TYPE)
    category = models.ForeignKey(Category, verbose_name="categoria")
    conference = models.ManyToManyField(Conference, verbose_name="conferencia")

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __unicode__(self):
        return self.name

admin.site.register(Category)
admin.site.register(Conference)
admin.site.register(Event)
