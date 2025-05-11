from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=50)
    asosiy = models.BooleanField(blank=True, null=True)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField(default=18)
    jins = models.CharField(max_length=20, choices=(("Erkak", "Erkak"), ("Ayol", "Ayol")))
    daraja = models.CharField(max_length=20, choices=(("Bakalavr", "Bakalavr"), ("Magistr", "Magistr")))
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.ism


