from .settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*@j$ybt^n#)%hu^us^ea@!2@3!@%^e^qj-h=(-4m_r%nj&4he5'

ALLOWED_HOSTS = ['domain-example.com']

DEBUG = False

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
MEDIA_ROOT = os.path.join(BASE_DIR, "media_root")

DISQUS_API_KEY = 'FOOBARFOOBARFOOBARFOOBARFOOBARF'
DISQUS_WEBSITE_SHORTNAME = 'pythontijuana'
SITE_ID = 1

GOOGLE_ANALYTICS_ID = 'FOOBARFOOBARFOO'
