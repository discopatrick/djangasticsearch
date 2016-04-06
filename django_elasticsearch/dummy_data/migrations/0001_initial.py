# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests

from django.db import migrations, models

from django_elasticsearch import settings

def import_contacts(apps, schema_data):
	Contact = apps.get_model('contacts', 'Contact')

	r = requests.get(
		'http://api.randomuser.me/?results=%s&key=%s&seed=%s&nat=%s' %
		(settings.RANDOM_USER_COUNT,
		settings.RANDOM_USER_API_KEY,
		settings.RANDOM_USER_SEED,
		settings.RANDOM_USER_LOCALE)
	)

	for result in r.json()['results']:
		contact = Contact()
		contact.first_name = result['user']['name']['first']
		contact.last_name = result['user']['name']['last']
		contact.save()

class Migration(migrations.Migration):

    dependencies = [
    	('contacts', '0002_add_name_fields'),
    ]

    operations = [
    	migrations.RunPython(import_contacts),
    ]
