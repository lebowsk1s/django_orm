# -*- coding: utf-8 -*-
# Django specific settings
import django
from django.conf import settings
import djsettings as s

settings.configure(DATABASES=s.DATABASES, INSTALLED_APPS=['django_orm.app'], DEBUG=True)
django.setup()
