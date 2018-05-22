# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doc(models.Model):
    
    rated = models.BooleanField(default=False)

    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    
    ratedBy = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    isNew = models.BooleanField(blank=True, choices=BOOL_CHOICES, default=False, verbose_name = "Article Mentions New Product?")
    
    # Other Shit
    article_title = models.TextField()
    subject	= models.TextField()
    company	= models.TextField()
    publication_title = models.TextField()
    publication_date = models.DateField(null=True)
    publication_subject = models.TextField()
    source_type = models.TextField()
    document_type = models.TextField()
    html = models.TextField()