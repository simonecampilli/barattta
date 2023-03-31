from django.db import models
class Persona(models.Model):
    STATI = (
        ('S', 'Single'),
        ('I', 'Impegnato'),
        ('O', 'Occupato'),
    )
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)
    codice_fiscale = models.CharField(max_length=16)
    stato = models.CharField(max_length=1, choices=STATI)
    nome_instagram = models.CharField(max_length=255)