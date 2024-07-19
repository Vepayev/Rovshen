from django.db import models

class Insert(models.Model):
    no = models.AutoField(primary_key=True)
    senesi = models.DateField()
    gelen_tyr = models.CharField(max_length=255, blank=True, null=True)
    gelen_haryt = models.CharField(max_length=255, blank=True, null=True)
    acylan_tyr = models.CharField(max_length=255, blank=True, null=True)
    cykan_haryt = models.CharField(max_length=255, blank=True, null=True)
    cykman_duran_haryt = models.CharField(max_length=255, blank=True, null=True)
    deklerant_algy = models.CharField(max_length=255, blank=True, null=True)
    bellik = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Insert {self.no}"

