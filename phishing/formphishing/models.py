from django.db import models

# Create your models here.
# models.py

from django.db import models

class Usuario(models.Model):
    correo_corporativo = models.EmailField()
    clave = models.CharField(max_length=100)
   
    def __str__(self):
        return self.correo_corporativo
