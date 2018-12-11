# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class NuomiMovie(models.Model):
    title = models.CharField(primary_key=True, max_length=200)
    score = models.CharField(max_length=100, blank=True, null=True)
    daoyan = models.CharField(max_length=200, blank=True, null=True)
    zhuyao = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    republish_date = models.CharField(max_length=200, blank=True, null=True)
    runtime = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nuomi_movie'

    def __str__(self):
        return self.title
