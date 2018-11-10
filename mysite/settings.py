import os
from mysite import secrets

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

    # Application definition

    # WARNING: test_without_migrations app must appear before any other apps
    # in INSTALLED_APPS that provide a custom test management command.
    # See https://pypi.org/project/django-test-without-migrations/

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'heritagesites.apps.HeritagesitesConfig',
    'crispy_forms',
    'social_django',
    'test_without_migrations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.open_id.OpenIdAuth',
    # 'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.yahoo.YahooOpenId',
    'django.contrib.auth.backends.ModelBackend',
)

    # Add a custom test runner for converting unmanaged models to managed before
    # running a test and then revert the effect afterwards.

TEST_RUNNER = 'heritagesites.utils.UnManagedModelTestRunner'

    # test_without_migration setting that ensures you don’t lose any additional
    # functionality provided by your custom test management command.

    # TEST_WITHOUT_MIGRATIONS_COMMAND = 'django_nose.management.commands.test.Command'

WSGI_APPLICATION = 'mysite.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unesco_heritage_sites',
        'USER': 'laurensheridan',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
    }
}

    # Password validation
    # https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

    # Internationalization
    # https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'
    # TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.1/howto/static-files/
    # https://stackoverflow.com/questions/8687927/django-static-static-url-static-root

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static")

TEST_RUNNER = 'heritagesites.utils.UnManagedModelTestRunner'

CRISPY_TEMPLATE_PACK = 'bootstrap4'
