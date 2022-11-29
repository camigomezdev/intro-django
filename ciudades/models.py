from django.conf import settings
from django.db import models
from django.utils import timezone


class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='ciudades/fotos',
                             height_field=None, width_field=None, max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Comment(models.Model):
    city = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField(default=0)
