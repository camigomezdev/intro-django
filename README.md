# Ejercicio práctico de Django

## Instalación:

```
python -m venv venv
source venv/bin/activate # Para Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Para crear un super usuario y acceder al admin:

```
python manage.py createsuperuser
```

## Diagrama de la base de datos:

![Diagrama base de datos](docs/db.PNG)
