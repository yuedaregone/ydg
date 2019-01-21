# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Skv(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    key = models.TextField(blank=True, null=True)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Skv'

