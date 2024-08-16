from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-_vgt4t#-$^xqt3blm4@3b*#o9b_kjkblb@m4^wno(pj0k*4tq^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # installed
    "tinymce",
    "rest_framework",
    # 'rest_framework_simplejwt',
    # experemental
    "corsheaders",
    "api_blog",
    "api_courses",
    "api_python",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # corse header
    "corsheaders.middleware.CorsMiddleware",
    # front of csrf header
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "LTS.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "LTS.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# corse header
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:8000",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


TINYMCE_DEFAULT_CONFIG = {
    "height": 360,
    "width": "100%",
    "plugins": "code codesample",
    "toolbar": "undo redo | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | codesample | code",
    "menubar": False,
    "statusbar": True,
    "statusbar": True,
    "content_style": "pre { white-space: pre-wrap; }",  # Ensures the formatting is preserved
    "extended_valid_elements": "pre[class|name|style]",
    "codesample_languages": [
        {"text": "Python", "value": "python"},
        {"text": "JavaScript", "value": "javascript"},
        {"text": "HTML/XML", "value": "markup"},
        {"text": "CSS", "value": "css"},
    ],
    # "automatic_uploads": True,
    # "file_picker_types": "image",
}

# TINYMCE_DEFAULT_CONFIG = {
#     "height": 500,
#     "width": "100%",
#     "plugins": "code image imagetools",
#     "toolbar": "undo redo | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | code image | removeformat",
#     "menubar": False,
#     "statusbar": True,
#     "image_caption": True,
#     "image_advtab": True,
#     "content_style": "pre { white-space: pre-wrap; } img { max-width: 100%; height: auto; }",  # Ensure formatting and image responsiveness
#     "extended_valid_elements": "pre[class|name|style],img[alt|src|class|title|width|height]",
#     "automatic_uploads": True,
#     "file_picker_types": "image",
# }
