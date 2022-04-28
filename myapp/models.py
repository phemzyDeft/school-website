from tabnanny import verbose
from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ="Feature"
