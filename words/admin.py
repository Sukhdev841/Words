# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from words.models import Word
from words.models import Quote
from words.models import Reading

# Register your models here.

admin.site.register(Word)
admin.site.register(Quote)
admin.site.register(Reading)