"""
Settings for django-facebook
"""
import facebook
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import get_user_model

User = get_user_model()

try:
    APP_ID = getattr(settings, 'FACEBOOK_APP_ID')
    APP_SECRET = getattr(settings, 'FACEBOOK_APP_SECRET')
    REDIRECT_URI = getattr(settings, 'FACEBOOK_REDIRECT_URI')
except AttributeError:
    raise ImproperlyConfigured('You need to set FACEBOOK_APP_ID, '
        'FACEBOOK_APP_SECRET and FACEBOOK_REDIRECT_URI to use django-facebook')

BACKEND_STR = 'django_facebook.auth.FacebookModelBackend'										# String version of the location to the Facebook Authentication class
USER_MODEL_FACEBOOK_ID = getattr(settings, 'USER_MODEL_FACEBOOK_ID', User.USERNAME_FIELD)		# Field on the user model that stores the facebook_id
FACEBOOK_CREATE_ACCOUNT = getattr(settings, 'FACEBOOK_CREATE_ACCOUNT', False)

VERSION = getattr(settings, 'FACEBOOK_VERSION', "2.2")
auth = facebook.Auth(APP_ID, APP_SECRET, REDIRECT_URI, VERSION)
COOKIE_NAME = 'fbsr_%s' % APP_ID
CANVAS_PAGE = getattr(settings, 'FACEBOOK_CANVAS_PAGE', "")
DEBUG_SIGNEDREQ = getattr(settings, 'FACEBOOK_DEBUG_SIGNEDREQ', "")
DEBUG_COOKIE = getattr(settings, 'FACEBOOK_DEBUG_COOKIE', "")
DEBUG_TOKEN = getattr(settings, 'FACEBOOK_DEBUG_TOKEN', "")
