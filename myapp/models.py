from django.db import models
from django.core.exceptions import ValidationError

class Wydatek(models.Model):
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.CharField(max_length=100)
    data = models.DateField()  # Dodajemy pole data

    def __str__(self):
        return f"{self.data} - {self.kwota} zł ({self.kategoria})"

    def clean(self):
        if self.kwota >= 0:
            raise ValidationError("Kwota wydatku musi być MNIEJSZA od zera.")
class Dochod(models.Model):
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.CharField(max_length=100)
    data = models.DateField()  # Data uzyskania dochodu
    def __str__(self):
        return f"  {self.kwota} zł ({self.kategoria} )"
    def clean(self):
        if self.kwota <= 0:
            raise ValidationError("Kwota dochodu musi być większa od zera.")

class Oszczednosc(models.Model):
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    kategoria = models.CharField(max_length=100)
    def __str__(self):
        return f"  {self.kwota} zł ({self.kategoria})"
    def clean(self):
        if self.kwota <= 0:
            raise ValidationError("Kwota Oszczednosci musi być większa od zera.")

class Przypomnienie(models.Model):
    tytuł = models.CharField(max_length=200)
    opis = models.TextField(blank=True, null=True)
    data_przypomnienia = models.DateField()

    def __str__(self):
        return f"{self.tytuł} - {self.data_przypomnienia} - {self.opis}"
