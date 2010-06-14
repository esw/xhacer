try:
    from djangoappengine.settings_base import *
    has_djangoappengine = True
except ImportError:
    has_djangoappengine = False
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    
import os
import sys

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
APPS_DIR = os.path.join(PROJECT_DIR,'apps')
EXT_APPS_DIR = os.path.join(PROJECT_DIR,'ext_apps')
TEMPLATES_DIR = os.path.join(PROJECT_DIR,'templates')

sys.path.append(APPS_DIR)
sys.path.append(EXT_APPS_DIR)

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'base.context_processors.base_settings',
)

INSTALLED_APPS = (
    'djangotoolbox',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    #'emailconfirmation',
    #'account',
    
    'geo',
    'places',
)

if DEBUG:
    _ds_pathinfo = {
        'datastore_path' : 'gae-data/dgae.datastore',
        'history_path' : 'gae-data/dgae.datastore.history',
    }
    DATABASES['default'].update(_ds_pathinfo)

if has_djangoappengine:
    INSTALLED_APPS = ('djangoappengine',) + INSTALLED_APPS

ROOT_URLCONF = 'urls'

LOGIN_URL = "/login"
LOGIN_REDIRECT_URL = "/"

ADMIN_MEDIA_PREFIX = '/media/admin/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (TEMPLATES_DIR,)

GOOGLE_MAPS_API_KEY = 'ABQIAAAAzr2EBOXUKnm_jVnk0OJI7xSosDVG8KKPE1-m51RBrvYughuyMxQ-i1QfUnH94QxWIa6N4U6MouMmBA'
MAPS_API_KEY = GOOGLE_MAPS_API_KEY