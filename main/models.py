from django.db import models

class Yonalish(models.Model):
    nom = models.CharField(max_length=255)
    aktiv = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = 'Yonalish'
        verbose_name_plural = 'Yonalishlar'

    def __str__(self):
        return self.nom

class Fan(models.Model):
    nom = models.CharField(max_length=50)
    asosiy = models.BooleanField(blank=True, null=True)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Fan"
        verbose_name_plural = "Fanlar"

    def __str__(self):
        return self.nom

class Ustoz(models.Model):
    JINS_TANLASH = (("Erkak", "Erkak"), ("Ayol", "Ayol"))
    DARAJA = (("Bakalavr", "Bakalavr"), ("Magistr", "Magistr"))
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField(default=18)
    jins = models.CharField(max_length=20, choices=JINS_TANLASH)
    daraja = models.CharField(max_length=20, choices=DARAJA)
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'Ustoz'
        verbose_name_plural = 'Ustozlar'

    def __str__(self):
        return self.ism


