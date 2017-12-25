# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class ExceptionWord(models.Model):
	word = models.CharField(max_length=30)

class Word(models.Model):
	word = models.CharField(max_length = 30)
	meaning = models.CharField(max_length = 500,default='english')
	hindi = models.CharField(max_length = 500,default='hindi')
	punjabi = models.CharField(max_length = 500,default='punjabi')
	sentence = models.CharField(max_length = 200,default='example sentence')
	date = models.DateTimeField(("Date"),default=datetime.date.today)
	tags = models.CharField(max_length=1000,default='word')

class Quote(models.Model):
	#quote_id = models.CharField(max_length=600,default='1')
	quote = models.CharField(max_length = 500)
	author = models.CharField(max_length = 50)
	language = models.CharField(max_length = 30,default='English')
	date = models.DateTimeField(("Date"),default=datetime.date.today)
	tags = models.CharField(max_length=1000,default='quote')

class Reading(models.Model):
	heading = models.CharField(max_length = 50)
	passage = models.CharField(max_length = 10000)
	author = models.CharField(max_length = 50)
	language = models.CharField(max_length = 50,default='English')
	tags = models.CharField(max_length = 1000,default = 'passage')
	date = models.DateTimeField(("Date"),default = datetime.date.today)