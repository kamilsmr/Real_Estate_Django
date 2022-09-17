from django.db import models

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

