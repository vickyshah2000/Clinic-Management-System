"""
WSGI config for clinic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinic.settings')
import sys
sys.path.append('C:\\Users\\vikas\\Downloads\\Clinic_Management_System_Project_Django.zip\\Clinic_Management_System_Project_Django')
application = get_wsgi_application()
