# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models, migrations

#from django.contrib.auth.models import User
from django.contrib.auth.management.commands.createsuperuser import get_user_model

username = os.environ.get('admin_name')
password = os.environ.get('admin_password')
if get_user_model().objects.filter(username=username): 
    print ('Super user already exists. SKIPPING...')
else:
    print ('Creating super user...')
    # User.objects.create_superuser(username=username, password=password)
    get_user_model()._default_manager.db_manager('default').create_superuser(username=username, email='default', password=password)
    print ('Super user created...')
class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
    ]
