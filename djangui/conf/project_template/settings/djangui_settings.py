from .django_settings import *

INSTALLED_APPS += (
    # 'corsheaders',
    'djguicore',

    '{{ app_name }}',
)

# MIDDLEWARE_CLASSES = [[i] if i == 'django.middleware.common.CommonMiddleware' else ['corsheaders.middleware.CorsMiddleware',i] for i in MIDDLEWARE_CLASSES]
# MIDDLEWARE_CLASSES = [j for i in MIDDLEWARE_CLASSES for j in i]

PROJECT_NAME = "{{ project_name }}"
DJANGUI_CELERY_APP_NAME = '{0}.celery'.format(PROJECT_NAME)
DJANGUI_CELERY_TASKS = '{0}.tasks'.format(PROJECT_NAME)