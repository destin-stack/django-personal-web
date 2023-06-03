from .base import *

DEBUG = True

# Database Config
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Override Installed Apps
# If we want to add new app, we can added it on the list, so the base config stay the same
INSTALLED_APPS += [
    'blog.apps.BlogConfig'
]

