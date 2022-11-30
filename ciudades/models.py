from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


class City(models.Model):
    name = models.CharField(max_length=200)
    country = CountryField()
    description = models.TextField()
    image = models.ImageField(upload_to='ciudades/fotos',
                             height_field=None, width_field=None, max_length=100)

    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'

class Comment(models.Model):
    city = models.ForeignKey('ciudades.City', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
