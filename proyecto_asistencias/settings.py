import os
from pathlib import Path
from dotenv import load_dotenv

# ========================
# CONFIGURACIÓN BASE
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables del archivo .env
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'clave-secreta-django-desarrollo')

DEBUG = True

ALLOWED_HOSTS = ['*']  # Cambia esto en producción

# ========================
# APLICACIONES INSTALADAS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'asistencias',            # Nuestra app principal
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# URL PRINCIPAL
# ========================
ROOT_URLCONF = 'proyecto_asistencias.urls'

# ========================
# TEMPLATES
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'asistencias' / 'templates'],  # Ruta a tus templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ========================
# WSGI
# ========================
WSGI_APPLICATION = 'proyecto_asistencias.wsgi.application'

# ========================
# BASE DE DATOS
# ========================
# Por defecto usa SQLite, pero puedes cambiar fácilmente a MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'asistencias.db',
    }
}

"""
# Si prefieres MySQL, reemplaza por esto:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'asistencias_db'),
        'USER': os.getenv('DB_USER', 'root'),
        'PASSWORD': os.getenv('DB_PASS', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '3306'),
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}
"""

# ========================
# VALIDACIÓN DE CONTRASEÑAS
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# INTERNACIONALIZACIÓN
# ========================
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ========================
# ARCHIVOS ESTÁTICOS
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'asistencias' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ========================
# ARCHIVOS SUBIDOS (MEDIA)
# ========================
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ========================
# CONFIGURACIÓN DE SESIONES
# ========================
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# ========================
# CONFIGURACIÓN EMAIL (opcional)
# ========================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# ========================
# CONFIGURACIÓN FINAL
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

