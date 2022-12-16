# Ejercicio práctico de Django

## Instalación:

```
python -m venv venv

# Activación en Unix
source venv/bin/activate

# Activación en Windows
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Para crear un super usuario y acceder al admin:

```
python manage.py createsuperuser
```

## Base de datos:

Esto proyecto requiere que tenga instalado MySQL.
Actualice los datos de la base de datos que quiere utilizar en `settings.py`.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_de_datos',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': 'host',
        'PORT': 'port'
    }
}
```

docs: https://docs.djangoproject.com/en/4.1/ref/settings/#databases

## Diagrama de la base de datos:

![Diagrama base de datos](docs/db.PNG)
