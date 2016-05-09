# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.db import migrations, models

def import_words(apps, schema_data):
	Word = apps.get_model('words', 'Word')

	r = requests.get('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt')

	for line in r.text.splitlines():
		word = Word()
		word.word_string = line
		word.save()

class Migration(migrations.Migration):

    dependencies = [
    	('dummy_data', '0001_import_contacts'),
        ('words', '0001_initial'),
    ]

    operations = [
    	migrations.RunPython(import_words),
    ]
